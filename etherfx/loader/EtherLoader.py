import sys
from etherfx.classes.ProxyModule import ProxyModule

class EtherLoader(object):
    def __init__(self):
        pass
    
    def find_module(self, fullname, path=None):
        if 'ether' in fullname:
            #Add netcode to check if module exists
            return self
        return None

    def load_module(self, name):
        module = ProxyModule(name)
        module.__loader__ = self
        sys.modules[name] = module
        return module