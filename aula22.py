# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

""" entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
Senha_permitida= '123456'

if (entrada == 'E' or entrada == 'e')  and senha_digitada == Senha_permitida:
    print('Entrou')
else:
    print('Sair') """


print(True or False )

senha = input('Senha: ') or ('senha senha')
print(senha)
