""" while/else """

string = 'Valorqualquer'

i = 0

while i < len(string):
    letra = string[i]
    print(letra)
    if letra == ' ':
        break
    i += 1
else:
    print('Não encontrei nenhum espaço')
