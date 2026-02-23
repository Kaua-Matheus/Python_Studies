from functools import partial
from typing import Callable

power = lambda x, expo: x ** expo
summer = lambda x, y, z: x + y + z

# Implementação de partial
square_partial = partial(power, expo=2)
cube_partial = partial(power, expo=3)

print(f"Square: {square_partial(2)}")
print(f"Cube: {cube_partial(2)}")


# Implementação de partial manual
class partial_manual:
    def __init__(self, func: Callable, **params):
        self.func = func
        self.params = params

    def __call__(self, **x):
        return self.func(**x, **self.params)

part = partial_manual(summer, y=2, z=3)
print(part(x=10))