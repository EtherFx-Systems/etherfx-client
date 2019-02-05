import importlib.util as imp
import sys
import types

from ether._internal.classes.ProxyModule import ProxyModule


class EtherLoader(object):
    def __init__(self):
        pass
    
    def find_module(self, fullname, path=None):
        parent, sep, child = fullname.rpartition('.')
        if parent and parent == 'ether':
            #Add netcode to check if module exists
            return self
        elif fullname == 'ether':
            return self
        else:
            return None

    def load_module(self, fullname):
        _, sep, child = fullname.rpartition('.')
        module = ProxyModule(fullname)
        if fullname != 'ether':
            module.__dict__['__underlying__'] = self.try_import(fullname)
        else:
            module.__path__ = []
        module.__loader__ = self
        sys.modules[fullname] = module
        return module

    def try_import(self, module_name):
        _, _, child = module_name.rpartition('.')
        spec = imp.find_spec(child)
        if spec is None:
            raise ImportError(f"Module {child} isn't installed. Please install {child} and try again.")
        module = imp.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

