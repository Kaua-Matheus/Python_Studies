from datetime import datetime as dt
from contextlib import contextmanager

def charge_function():
    c = 2
    for i in range(10000000):
        c = c ** i


# Aplicando Context com Class
class Timer:
    def __enter__(self):
        self.start_time = dt.now()
        return self

    def __exit__(self, *args):
        print(f"Processo finalizado..")
        print(f"Process time: {dt.now() - self.start_time}")
        pass



with Timer() as T:
    print("Executando processo...")
    charge_function()

# Corte de linha
print(
"\n\n"
)

# Também é possível aplicar Context com contextmanager
@contextmanager
def timer():
    start_time = dt.now()

    yield # Execução do bloco with

    print("Processo finalizado..")
    print(f"Process time: {dt.now() - start_time}")

with timer():
    print("Executando processo...")
    charge_function()



# Ambos os jeitos tendem a ser semelhantes no tempo de execução (em processos muito grandes, utilizando contextmanager pode ser mais rápido)