# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

print(multiplicar(1, 2, 3, 4))

def par_impar(x):
    calculo = x % 2
    if calculo == 0:
        return f'{x} é PAR'
    return f'{x} é IMPAR'

print(par_impar(3))

