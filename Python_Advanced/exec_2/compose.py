from typing import Callable

def compose(x, *funcs:Callable):
    entry = x
    for f in funcs:
        print(f"Retorno: {f(entry)}")
        entry = f(entry)

    return entry


func_1 = lambda x: x + 1
func_2 = lambda x: x * 2
func_3 = lambda x: x + 3


compose(1, func_1, func_2, func_3)