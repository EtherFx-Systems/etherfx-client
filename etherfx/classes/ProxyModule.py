from types import ModuleType
import importlib.util as imp
#Inspired: https://github.com/pallets/werkzeug/blob/master/werkzeug/__init__.py
class ProxyModule(ModuleType):
    @classmethod
    def is_proxy(self): #Flag ourselves as the proxy
        return True

    def __getattribute__(self, name):
        if name == '__underlying__':
            return self.__dict__[name]
        elif name != '__dict__':
            return self.__underlying__.__getattribute__(name)
        else:
            return super().__getattribute__(name)
    
    def __dir__(self):
        pass #classes from ether
