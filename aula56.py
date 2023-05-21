"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

frase = '   Se hoje não chover    , vai estar um dia lindo!  '

lista_frase = frase.split(',')
print(lista_frase)

nova_lista_sem_espacos = []
for i, frase in enumerate(lista_frase):
    nova_lista_sem_espacos.append(frase.strip())

print(nova_lista_sem_espacos)

frases_unidas = " - ".join(nova_lista_sem_espacos)
print(frases_unidas)