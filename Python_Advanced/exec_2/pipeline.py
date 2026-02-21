from typing import Callable, TypeVar, Generic

# Definindo genérico
T = TypeVar("T")

class Type:
    def __init__(self, class_type, func: Callable):
        self.class_type = class_type
        self.func = func


class Pipeline:
    def __init__(self, array: list, *func: tuple[Generic[T], Callable]):
        """
        O pipeline deve adquirir diferentes funções e executa-las em um array, retornando o resultado já completamente processado.
        """

        self.array = array
        self.func = func

    def __next__(self):
        for f in self.func:
            self.array = list(f[0](f[1], self.array))

        return self.array


doubleit = lambda x: x * 2
powerit = lambda x: x ** 2
minor10 = lambda x: True if x < 10 else False

print(next(Pipeline([1, 2, 3, 9, 10, 11], (filter, minor10), (filter, minor10))))