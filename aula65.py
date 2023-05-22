"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

def nome_da_funcao():
    print('Função executada')

nome_da_funcao()



def funcao_1(a, b, c):  #  a, b e c são os parametros
    print(a, b, c)



funcao_1(1, 2, 3)   #  1, 2 3 e são os argumentos
funcao_1(4, 5, 6)


def saudacao(nome = 'Sem nome'):
    print(f'Ola {nome}')

saudacao('Nuno')
saudacao()

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)