"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

variavel = 'Olá Mundo!'

print(variavel[2:3])
print(variavel[:3])
print(variavel[:-3])
print(variavel[0:9:2])
print(variavel[::-1])
print(len(variavel))