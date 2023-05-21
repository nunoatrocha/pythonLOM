"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

print('Valor' if True else 'Outro valor')

condicao_1 = 10 == 10
variavel = 'Valor_verdadeiro' if condicao_1 else 'Valor_falso'
print(variavel)

condicao_2 = 10 == 11
variavel = 'Valor_verdadeiro' if condicao_2 else 'Valor_falso'
print(variavel)

digito = 13 # > 9 = 0 
novo_digito = digito if digito <= 9 else 0
print(novo_digito)