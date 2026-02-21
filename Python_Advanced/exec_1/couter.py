"""
    couter: Dado um texto gigante, conte palavras usando:
    - dict normal
    - collections.Counter
    - versão otimizada com defaultdict
"""

# Collections Couter
"""
A biblioteca Collections é uma build-in do python que adiciona mais funcionalidades aos tipos primários de ordenação (lista, tuplas e dicionários)
Utilizar collections otimiza os processos visto que as funções / tipos são muito mais otimizados do que o padrão do python
"""

from collections import Counter, defaultdict

import string

# Essa lista possui os caracteres especiais mais importantes
char_list = [char for char in string.punctuation]


text = "Oi, eu sou o goku!"

# Tratamento inicial (Retirando os caracteres especiais)
for char in char_list:
    if char not in text:
        continue
    else:
        text = text.replace(char, "")


# Dicionário
dic_dict = dict()
for word in text.split(" "):
    if word.lower() not in dic_dict:
        dic_dict[word.lower()] = 1
    else:
        dic_dict[word.lower()] += 1


# Couter
dic_couter = Counter([item.lower() for item in text.split(" ")])


# DefaultDict
dic_default = defaultdict(int)
for word in text.split(" "):
    dic_default[word.lower()] += 1


print(f"Diferentes maneiras de contabilizar!")
print(f"Dict: {dic_dict}")
print(f"Couter: {dic_couter}")
print(f"DefaultDict: {dic_default}")