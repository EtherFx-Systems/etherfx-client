from ether._internal.core.Promise import Promise
from inspect import getmodule
from ether._internal.core.net.grpc_client import TaskClient
from ether._internal.cli import get_config


class ProxyFunction:
    __task_client = TaskClient(get_config().host, get_config().port)
    def __init__(self, name, function, obj = None):
        self.__function = function
        self.__name = name
        self.__obj = obj

    def __call__(self, *args, **kwargs):
        promise = Promise(getmodule(self.__function).__name__,
                          self.__name,
                          args,
                          kwargs,
                          _class = self.__obj.__class__.__name if self.__obj else None)
        promise.ether_send(self.__task_client)
        return promise
        #return self.__function(*args, **kwargs)