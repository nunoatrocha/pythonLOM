# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

count_acertos = 0

for pergunta in perguntas:
    print("Pergunta: ", pergunta['Pergunta'])
    print("Opções:")

    for index, opcao in enumerate(pergunta['Opções']):
        print(f'{index}) - {opcao}')

    qdt_opcoes = len(pergunta['Opções'])

    escolha = input('Escolha uma opção: ')
    escolha_inteiro = None
    if escolha.isdigit():
        escolha_inteiro = int(escolha)
        
    if escolha_inteiro is not None:
        if escolha_inteiro >= 0 and escolha_inteiro  < qdt_opcoes:
            if pergunta['Opções'][escolha_inteiro] == pergunta['Resposta']:
                count_acertos += 1
                print('Acertou')
            else:
                print('Errou')

print(f'Você acertou {count_acertos} de {len(perguntas)} perguntas.')
