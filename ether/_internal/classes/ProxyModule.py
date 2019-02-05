from types import ModuleType
import inspect
import importlib.util as imp
from ether._internal.classes.ProxyClass import ClassProxy
#Inspired: https://github.com/pallets/werkzeug/blob/master/werkzeug/__init__.py
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
                return ClassProxy(attr)
            else:
                return attr
        else:
            return super().__getattribute__(name)
    
    def __dir__(self):
        return self.__underlying__.__dir__()


