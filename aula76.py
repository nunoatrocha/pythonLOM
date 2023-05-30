# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

pessoa = {
    'nome': 'Nuno',
    'sobrenome': 'Rocha',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
         {'rua': 'tal tal', 'número': 123},
         {'rua': 'outra rua', 'número': 321},
     ]
}

print(pessoa['nome'])
print(pessoa['endereços'])

for chave in pessoa:
    print(chave, pessoa[chave])

pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'


print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')


# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro


pessoa = {
    'nome': 'Nuno',
    'sobrenome': 'Rocha',
    'idade': 900,

}

print(len(pessoa))
print(pessoa.keys())
print(list(pessoa.keys()))
print(pessoa.values())
print(list(pessoa.values()))
print(pessoa.items())
print(list(pessoa.items()))
print(pessoa['idade'])

import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': ['Nuno', 'Rocha']
}

d2 = d1.copy()

d3 = copy.deepcopy(d1)  # copia profunda
d3['l1'][0] = 'Alexandre'

d2['c1'] = 1000
d2['l1'][0] = 'Pedro'

print(d1)
print(d2)
print(d3)

#################################

p1 = {
    'nome': 'Nuno',
    'sobrenome': 'Rocha'
}

print(p1['nome'])
#  ou
print(p1.get('nome')) 


#nome = p1.pop('nome')
#print(nome)
#print(p1)

#nome = p1.popitem()
#print(nome)
#print(p1)


p1.update({
    'nome': 'Pedro',  #   ou  p1.update(nome= 'Pedro', idade= 44)
    'idade': 44
})

print(p1)