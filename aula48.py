"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [123, True, 'python', 1.8]

print(lista, type(lista))
print(lista[2].upper())

lista_2 = [10, 20, 30, 40]
print(lista_2[2])

lista_2[2] = 300

print(lista_2[2])

del lista_2[2]

print(lista_2)
lista_2.append(50)
print(lista_2)

lista_2.pop()
print(lista_2)

lista_2.insert(0, 5)
print(lista_2)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b
print(lista_c)

lista_a.extend(lista_b)
print(lista_a)