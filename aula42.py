frase = 'O Python é cool'

i = 0
letra_apareceu_mais_vezes = ' '
quantidade_letra_apareceu_mais_vezes = 0

while i < len(frase):
    letra_atual = frase[i]
    quantidade_letra_apareceu = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue


    if quantidade_letra_apareceu_mais_vezes < quantidade_letra_apareceu:
        quantidade_letra_apareceu_mais_vezes = quantidade_letra_apareceu
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f'A letra "{letra_apareceu_mais_vezes}" foi a que apareceu mais vezes com {quantidade_letra_apareceu_mais_vezes}')
