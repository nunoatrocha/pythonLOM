# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

nome = 'Otávio'

print(nome[2])   #  á
print(nome[-4])  #  á


print('á' in nome)
print('O' not in nome)

frase = 'O rato roeu a rolha do Rei da Russia'
escolha = input('Escolha a palvra o letra que pretende encontrar: ')

if escolha in frase:
    print(f'{escolha} está na frase')
else:
    print(f'{escolha} não está na frase')

lista_nomes = ['Steve', 'Jobs', 'Apple']

print('jobs' in lista_nomes)

print(lista_nomes.index('Jobs'))
