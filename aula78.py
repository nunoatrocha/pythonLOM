# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')

#s1 = set()  # vazio
#s1 = {'Luiz', 1, 2, 3}  # com dados
#print(type(s1), s1)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
"""
l1 = [1, 2, 2, 3, 4, 4, 2, 2, 1, 3, 3, 9, 5, 6, 6, 7, 8, 9, 9]
print(l1)
s2 = set(l1)
print(s2)
l1 = list(s2)
print(l1)
print(2 in l1)

# s1.clear()
s1.discard('Olá mundo')
s1.discard('Luiz')
print(s1)
"""

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2  # união | união (union) - Une
print(s3)  # {1, 2, 3, 4}
s3 = s1 & s2  # intersecção & (intersection) - Itens presentes em ambos 
print(s3)  # {2, 3}
s3 = s2 - s1  # diferença - Itens presentes apenas no set da esquerda    
print(s3)  # {4}
s3 = s1 ^ s2  # diferença simétrica ^ - Itens que não estão em ambos   
print(s3)  # {1, 4}
