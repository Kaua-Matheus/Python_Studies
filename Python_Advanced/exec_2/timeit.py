from random import randint
from typing import Callable
from time import sleep
import datetime as dt


class Timeit:
    def __init__(self, func: Callable):
        self.func = func

    def __call__(self):
        first_time = dt.datetime.now()

        self.func()

        last_time = dt.datetime.now()
        print(f"Tempo total de processamento: {last_time - first_time}")


@Timeit
def exec():
    process_time = randint(1, 10)
    sleep(2)
    if process_time < 9:
        return "timeout"

    else:
        return "acontece"
    

exec()