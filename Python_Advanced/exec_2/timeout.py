from random import randint
from typing import Callable
from time import sleep


class Retry:
    def __init__(self, func: Callable):
        self.expo = 2
        self.func = func

    def __call__(self):
        while self.expo < 5:
            wait = ((2 + randint(1, 5)/10)**self.expo).__round__(2)
            resp = self.func()
            if resp == "timeout":
                print(f"Dormiu: {wait}s")
                sleep(wait)
            else:
                print(f"Execução terminou")
                return

            self.expo += 1
        
        print("Não foi possível concluir o processo.. [Timeout]")


@Retry
def exec():
    process_time = randint(1, 10)
    if process_time < 9:
        return "timeout"

    else:
        return "acontece"
    

exec()