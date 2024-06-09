from random import randint

def new_func():
    x = int(input('Digite o número de jogos: '))
    return x

x = new_func()

def criar_mega():
    aleatorio = []
    while len(aleatorio) < 6:
        numero = randint(1, 60)
        if numero not in aleatorio:
            aleatorio.append(numero)
            aleatorio.sort()
    return aleatorio


def quantidade_jogos(num):
    for _ in range(num):
        print(f'{"---"*8}\n{criar_mega()}')


quantidade_jogos(x)

input(f'{"---"*8}\nPressione qualquer tecla para sair!')
