"""
Introdução ao empacotamento e desempacotamento
"""
nomes = ['Maria', 'Helena', 'Luiz']

nome1, nome2, nome3 = nomes

print(nome1)

nomes_2 = ['Jorge','Pedro', 'Manuel' ]

nomes_2_1, *_ = nomes_2  # empacotou em _ numa lista com Pedro e Manuel

print(nomes_2_1, _)