# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
"""
def duplica (numero):
    return numero * 2

num1 = int(input('Digite um numero: '))
print(duplica(num1))
"""


def multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = multiplicador(2)


print(duplicar(6))