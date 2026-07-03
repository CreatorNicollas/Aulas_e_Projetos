from utilitarios import inicio_bonito, fim_bonito, temporizador
import random

inicio_bonito(f'Sejam Bem-vindos Senhoras e Senhores ao...')
temporizador(5)
inicio_bonito(f'Adivinhador de números')

# Adivinhando números
nome_jogador = input(f'Olá jogador, como gostaria de ser chamado? ')
quantidade_tentativas = int(input(f'Diga aqui para mim, quantas chances você quer ter? (1 - 10): '))

def adivinha_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = quantidade_tentativas

    while True:
        try:
            palpite = int(input(f'{nome_jogador} Vamos lá, faça seu palpite aqui com números de 1 - 100: '))

            if not 1 <= palpite <= 100:
                raise ValueError(f'{nome_jogador}, por favor digite um número válido.')

            if tentativas <= quantidade_tentativas:
                tentativas -= 1
                if tentativas < 0:
                    print(f'{nome_jogador}. Suas tentativas se encerraram')
                    break
                
            if palpite < numero_secreto:
                print(f'{nome_jogador}, esse número foi muito baixo, tente novamente')
            elif palpite > numero_secreto:
                print(f'{nome_jogador}, esse número foi muito alto, tente novamente')
            else:
                print(f'Meus parabéns {nome_jogador}, você acertou o número que era {numero_secreto} com apenas {tentativas} tentativas')
                break

        except ValueError as e:
            print(f'Entrada inválida {e}')

adivinha_numero()
fim_bonito(f'E esse é o jogo, se quiser dar palpites para o Dev de como ser alguém melhor, entre em contato pelo número: 4002-8922')