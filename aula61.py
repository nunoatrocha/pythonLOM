"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

cpf = '74682489070'
cpf_9_digitos = cpf[0:9]

count = 10
somatorio = 0

for numero in cpf_9_digitos:
    somatorio += count * int(numero)
    count -= 1

primeiro_digito = (somatorio * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
print(primeiro_digito)



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