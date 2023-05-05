""" Calculadora com while """


while True:
    numero_1 = int(input('Digite o primeiro numero: '))
    numero_2 = int(input('Digite o segundo numero: '))
    operador = input('Digite o operado: (+ - * / : ')
    if operador == '+':
        calculo = numero_1 + numero_2
        print(f'A soma de {numero_1} + {numero_2} = {numero_1 + numero_2}')

    sair = input('Digite a letra [s] para sair ou enter para mais calculos ').lower().startswith('s')
    if sair is True:
        break





