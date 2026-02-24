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

        if open("annotation.txt", "r").read() != f:
            f = open("annotation.txt", "r")
            f = f.read()
            show = True
            os.system("cls" if os.name == "nt" else "clear")

        time.sleep(2e-2)

except KeyboardInterrupt as K:
    print("\n\nEncerrando o programa..")