from types import ModuleType

#Inspired: https://github.com/pallets/werkzeug/blob/master/werkzeug/__init__.py
class ProxyModule(ModuleType):
    @classmethod
    def is_proxy(self): #Flag ourselves as the proxy
        return True

    def __getattr__(self, name):
        pass #out classes from ether
    
    def __dir__(self):
        pass #classes from ether