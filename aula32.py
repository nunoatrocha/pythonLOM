"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um numero inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('PAR')
    else:
        print('IMPAR')
else:
    print('Numero digitado não é inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input('Digite a hora atual: ')

if entrada.isdigit():
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
     print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    else:
        print('Bom noite')
else:
    print('Numero digitado não é inteiro')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu nome: ')

tamanho_nome = len(nome)
if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')
