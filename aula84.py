# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)



lista = [numero * 2 for numero in range(10)]
print(list(range(10)))
print(lista)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
print(produtos)
novos_produtos=[produto for produto in produtos]
print(*novos_produtos, sep="\n")

novos_produtos=[produto['nome'] for produto in produtos]
print(*novos_produtos, sep="\n")

novos_produtos=[produto['preco'] for produto in produtos]
print(*novos_produtos, sep="\n")

novos_produtos = []

print(*produtos[0].values())