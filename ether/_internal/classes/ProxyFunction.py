class ProxyFunction:
    def __init__(self, name, function):
        self.__function = function
        self.__name = name

    def __call__(self, *args, **kwargs):
        return self.__function(*args, **kwargs)