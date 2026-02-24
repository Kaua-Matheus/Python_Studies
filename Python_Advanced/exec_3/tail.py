import time
import os

f = open("annotation.txt", "r")
f = f.read()

print("Pressione 'Ctrl + C' para sair...\n\n")
try:
    show = True
    while True:
        # Adicionar script
        if show:
            print(str.join("\n", f.split("\n")[-10:]))
            show = False

        time.sleep(1)

except KeyboardInterrupt as K:
    print("\n\nEncerrando o programa..")