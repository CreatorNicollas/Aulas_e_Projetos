from utilitarios import inicio_bonito, fim_bonito, subtitulos, sistema_avaliacao

# Neste sistema vamos cadastrar diversos itens em um dicionário

inicio_bonito(f'Seja Bem vindo ao cadastro de itens, onde você poderá cadastrar os itens do seu sistema')

nome_user = input(f'Por favor, poderia informar como gostaria de ser chamado:\n')
volume_produtos = int(input(f'{nome_user}. Poderia informar a quantos tipos de produtos que será armazenado?\n'))

def cadastro():
    produtos = {}

    for i in range(volume_produtos):
        nome = input(f'{nome_user}. Digite o nome do produto: ')
        quantidade = int(input(f'{nome_user}. Informe a quantidade de {nome} que será armazenada: '))

        produtos[nome] = quantidade

    subtitulos(f'Dicionário de produtos: {produtos}')

cadastro()
fim_bonito(f'{nome_user}. Este meu código, simples, rápido e pratico, agradeço por usar ele. Se possivel deixe uma nota no campo a seguir pois isso me ajuda muito!')
sistema_avaliacao()