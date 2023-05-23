"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
print(falar_bom_dia('Nuno'))

print((criar_saudacao('Boa noite'))('Nuno'))