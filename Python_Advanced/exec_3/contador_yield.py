def contador():
    n = 0
    while True:
        yield n     # Pausa aqui e salva o estado (faz algo como um return)
        n += 1      # Quando chamada novamente, parte daqui, mantendo o estado anterior


gen = contador()
print(next(gen))    # 0
print(next(gen))    # 1
print(next(gen))    # 2