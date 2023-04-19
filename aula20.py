primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor é maior: {primeiro_valor}')
elif primeiro_valor == segundo_valor:
    print('Os valores são iguais')
else:
    print(f'O segundo valor é maior: {segundo_valor}')
