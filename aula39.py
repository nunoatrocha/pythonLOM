"""
Iterando strings com while
"""
#       012345678910
nome = 'João Otávio'  # Iteráveis
#      1110987654321

contador = 0
nova_string = ''
while contador < len(nome):
    nova_string += '*' + nome[contador]
    contador += 1
print(nova_string + '*')
