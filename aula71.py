"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""


def soma(*args):
    total = 0
    for item in args:
        total += item
    return total

print(soma(1, 2, 3, 4))

numeros = 1, 2, 3, 4, 5, 6, 7

print(sum(numeros))

print(soma(*numeros))