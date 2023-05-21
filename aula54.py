"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar:')
    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        try:
            indice_apagar = int(input('Qual o índice que pretende apagar? '))
            del lista[indice_apagar]
        except ValueError:
            print('Digite um numero inteiro.')
        except IndexError:
            print('Índice não existe na lista.')
        except Exception:
            print('Erro desconhecido.')
    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Lista vazia.')
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor escolha uma opção correta i, a ou l')

    