from datetime import datetime as dt
from contextlib import contextmanager

def count():
    c = 0
    while True:
        yield c
        c += 1


# Também é possível aplicar Context com contextmanager
@contextmanager
def timer():
    start_time = dt.now()

    yield # Execução do bloco with

    print("Processo finalizado..")
    print(f"Process time: {dt.now() - start_time}")


gen = count()

with timer():
    print("Executando processo...")
    print(next(gen))
    print(next(gen))
    print(next(gen))

print("\n\n")

with timer():
    print("Executando processo...")
    print(next(gen))
    print(next(gen))
    print(next(gen))



# Ambos os jeitos tendem a ser semelhantes no tempo de execução (em processos muito grandes, utilizando contextmanager pode ser mais rápido)