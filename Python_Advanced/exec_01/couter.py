"""
    couter: Dado um texto gigante, conte palavras usando:
    - dict normal
    - collections.Counter
    - versão otimizada com defaultdict
"""

import string

char_list = [char for char in string.punctuation]


text = "Oi, eu sou o goku!"

# Tratamento inicial
for char in char_list:
    if char not in text:
        continue
    else:
        text = text.replace(char, "")


# Dicionário
dict_couter = dict()
for word in text.split(" "):
    if word.lower() not in dict_couter:
        dict_couter[word.lower()] = 1
    else:
        dict_couter[word.lower()] += 1

print(dict_couter)


# Collections.Couter
# dict_couter = dict()
# for word in text.split(" "):
#     if word.lower() not in dict_couter:
#         dict_couter[word.lower()] = 1
#     else:
#         dict_couter[word.lower()] += 1

# print(dict_couter)