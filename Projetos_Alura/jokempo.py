from utilitarios import inicio_bonito, fim_bonito, temporizador
import random

# Jokempo contra a máquina
inicio_bonito(f'Bem vindo ao Pedra, Papel e Tesoura contra uma máquina, seria você capaz de vencer ela?\n')

nome_jogador = input(f'Olá, como gostaria de ser chamado? \n')

def retry():
    escolher = input(f'{nome_jogador} você gostaria de tentar novamente? (Y/N)\n').lower()

    if escolher == 'y':
        print(f'Certo então, aqui vamos nós novamente\n')
        jokempo()
    else:
        print(f'Certo {nome_jogador}, assim será\n')
        mensagem(f'Aqui encerramos essa rodada\n')

def mensagem(mensagem):
    print(mensagem)
    print(f'Então, {nome_jogador} o que você achou dessa jogo?\n')

def jokempo():

    opcoes = ["pedra", "papel", "tesoura"]
    escolha_máquina = random.choice(opcoes)
    escolha_jogador = input(f"Jogador {nome_jogador} faça sua escolha: pedra, papel ou tesoura? \n").lower()

    if escolha_jogador not in opcoes:
        mensagem(f'Por favor faça uma escolha escolha válida {nome_jogador}\n')
        return
    
    print(f'E a máquina escolheu...')
    temporizador(15)
    print(f'{escolha_máquina}')

    if escolha_jogador == escolha_máquina:
        mensagem(f'{nome_jogador} você consegiu empatar com máquina\n')
        retry()
    elif (
        (escolha_jogador == 'pedra' and escolha_máquina == 'tesoura') or
        (escolha_jogador == 'papel' and escolha_máquina == 'pedra') or
        (escolha_jogador == 'tesoura' and escolha_máquina == 'papel')
    ):
        mensagem(f'{nome_jogador} você venceu essa rodada, consegiu ganhar da máquina feita para ganhar')
        retry()
    else:
        mensagem(f'KKKKKK você nunca vencer aqui, a máquina sempre vence, diferente de você. Brincadeiras a parte, já dizia Mestre Yoda: "Fazer ou não fazer tentativa não há"\n')
        retry()

jokempo()
fim_bonito(f'O código é isso, se quiser procurar o dev e conhecer outros "Programas" que o Dev faz, ele cobra 300 reais a hora')