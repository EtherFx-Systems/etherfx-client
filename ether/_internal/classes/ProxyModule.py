from types import ModuleType
import inspect
import importlib.util as imp
from six import callable
from ether._internal.classes.ProxyClass import ProxyClassWrapper
from ether._internal.classes.ProxyFunction import ProxyFunction

defined_attrs = ['__proxy__', '__underlying__']
class ProxyModule(ModuleType):
    def __init__(self, name):
        super().__init__(name)
        self.__dict__['__proxy__'] = True
    def __getattribute__(self, name):
        if name in defined_attrs:
            return self.__dict__[name]
        elif name != '__dict__':
            attr = self.__underlying__.__getattribute__(name)
            if inspect.isclass(attr):
                return ProxyClassWrapper(attr)
            if callable(attr):
                return ProxyFunction(name, attr)
            if inspect.ismodule(attr):
                module = ProxyModule(f'{self.__name__}.{name}')
                module.__dict__['__underlying__'] = attr
                module.__loader__ = self.__loader__
                module.__path__ = []
                return module
            else:
                return attr
        else:
            return super().__getattribute__(name)
    
    def __dir__(self):
        return self.__underlying__.__dir__()


