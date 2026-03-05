def contador():
    c = 0
    while True:
        yield c
        c += 1


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
            cls._initialized = False

        return cls._instance
    
    def __init__(self, value=None):
        if not self._initialized:
            self.value = value
            self._initialized = True


s1 = Singleton(value=10)