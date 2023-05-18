"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz']

lista.append('Fernando')

print(lista)


for indice, nome in enumerate(lista):
    print(indice, nome)
