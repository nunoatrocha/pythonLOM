import random

cpf_9_digitos = ''
for i in range(9):
   cpf_9_digitos += str(random.randint(0, 9))

print(cpf_9_digitos)
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

print('CPF valido' if cpf_calculado == cpf_9_digitos else 'CPF invalido')
print(cpf_calculado)






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