class Singleton:
    __instance = None

    def __init__(self, n) -> None:
        self.n = n

    def __new__(cls, *args, **kwargs) -> 'Singleton':
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
