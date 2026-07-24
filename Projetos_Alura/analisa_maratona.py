from utilitarios import inicio_bonito, fim_bonito, subtitulos, sistema_avaliacao

# Sistema para analise de participantes de uma maratona

inicio_bonito(f'Sejam Bem vindos ao Analisador de Participantes de Maratona (APM)')

participantes = {}
nome_user = input(f'Poderia informar seu nome organizador?\n')

def mostra_participantes():

    while True:
        participante = input(f'{nome_user}, poderia informar o nome do participante: ')
        idade = int(input(f'Poderia informar a idade de {participante} agora: '))

        participantes[participante] = idade

        adicionar_mais = input(f'{nome_user} tem mais algum participante para adicionar? (Responda com S ou N)\n')

        if adicionar_mais != 's':
            print(f'{nome_user}, então estamos encerrando por aqui...\n')
            break

    subtitulos(f'Nome dos participantes cadastrados para a maratona: {', '.join(participantes.keys())}\n')
    subtitulos(f'Idade dos participantes cadastrados para a maratona: {', '.join(str(idade) for idade in participantes.values())}')
    subtitulos(f'Participantes e suas respectivas idades:')
    for nome, idade in participantes.items(): 
        print(f'- {nome}: {idade} anos')

mostra_participantes()
fim_bonito(f'E aqui se encerra o código do APM, onde tem apenas uma pequena utilidade, sendo ela bem básica e simples, pois não precisa de muitas coisas e também é uma prática do criador desse sistema')
sistema_avaliacao()