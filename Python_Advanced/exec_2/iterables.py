# Recrie o map, filter, reduce manualmente.

# typing é a biblioteca python que suporta diferentes tipos de módulos e tipos naturais do python
from typing import Callable
from functools import reduce


pets = ["lovita", "petta", "amora"]
animais = ["cavalo", "cachorro", "galinha"]

# Aplicação de MAP
animais_map = list(map(str.upper, animais + pets))
print(f"List com map: {animais_map}")

# Aplicação de MAP Manual
def mapping(func: Callable, *array: list) -> list:
    _new_list = list()
    for _list in array:
        _new_list += _list
    _new_list = [func(item) for item in _new_list]
    return _new_list

animais_mapping = mapping(str.upper, animais + pets)
print(f"List com map manual: {animais_mapping}\n")


# Aplicação de Filter
valores = [1, 2, 2, 3, 5, 66, 100, 12, 90, 64, 35, 7]

# Lambda
check = lambda val: val > 10
valores_filter = list(filter(check, valores))
print(f"Valores > 10 com filter: {valores_filter}")

# Aplicação de Filter Manual
valores_filtered = list()
for val in valores: 
    if check(val):
        valores_filtered.append(val)
    else:
        pass

print(f"Valores > 10 com filter manual: {valores_filtered}\n")


# Aplicação de Reduce
sum_custom = lambda v_1, v_2: v_1 + v_2

# Note que com reduce, podemos adicionar um valor para início
reduce_val = reduce(sum_custom, valores, 10)

# Também podemos obter o mesmo resultado com sum.

print(f"Valor com reduce: {reduce_val}")
print(f"Valor com sum: {sum(valores, 10)}")

# Aplicando Reduce Manual
def reduce_manual(func: Callable, *array: list, start:float=.0) -> float:
    reduce_val = start

    _new_list = list()
    for _list in array:
        _new_list += _list

    for val in _new_list:
        reduce_val = func(reduce_val, val)

    return reduce_val

print(f"Valor com reduce manual: {reduce_manual(sum_custom, valores, start=10)}\n")