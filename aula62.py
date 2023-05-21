"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""

cpf = '7468289070'
cpf_9_digitos = cpf[0:9]

count = 10
somatorio = 0

for numero in cpf_9_digitos:
    somatorio += count * int(numero)
    count -= 1

primeiro_digito = (somatorio * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

##############################################################################################

cpf_10_digitos = cpf_9_digitos + str(primeiro_digito)
count = 11
somatorio = 0

for numero in cpf_10_digitos:
    somatorio += count * int(numero)
    count -= 1

segundo_digito = (somatorio * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

###############################################################################################

cpf_calculado = cpf_10_digitos + str(segundo_digito)

print('CPF valido' if cpf_calculado == cpf else 'CPF invalido')



"""
cpf = "746.824.890-70"
lista = cpf.split('.')
remover_validador = lista[2].split('-')
lista.pop()
lista.append(remover_validador[0])
print(lista)
lista_final = ""
for i in lista:
    lista_final += i
print(lista_final)
count = 10
somatorio = 0
for numero in lista_final:
    mult = count * int(numero)
    somatorio += mult
    count -= 1
somatorio_mul = somatorio * 10
somatorio_resto = somatorio_mul % 11
primeiro_digito = 0 if somatorio_mul > 9 else somatorio_resto
print(primeiro_digito)

"""