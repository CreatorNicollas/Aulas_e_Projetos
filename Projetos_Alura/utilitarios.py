import os, time

'''Este documento contém funções que são utilizadas para marcar horários, temporizar e embelezar os textos dos programas testes e outros.'''

# Marcador de horário
def horario_inicial():
    horario_atual = time.localtime()
    hora_formatada = time.strftime('%H:%M', horario_atual)

    print(f'Iniciando o programa às {hora_formatada} horas.')

def horario_final():
    horario_atual = time.localtime()
    hora_formatada = time.strftime('%H:%M', horario_atual)

    print(f'Encerrando o programa às {hora_formatada} horas.')

# Temporizadores
def temporizador(tempo):
    time.sleep(tempo)

# Embelezador de Textos
def inicio_bonito(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(f'* {texto} *')
    print(linha)
    horario_inicial()
    print()

def fim_bonito(texto):
    linha = '*' * (len(texto) + 4)
    print()
    horario_final()
    print(linha)
    print(f'* {texto} *')
    print(linha)

def subtitulos(texto):
    linha = '=' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

# Sistema de avaliação para os meus atuais e futuros sistemas

def sistema_avaliacao():

    respostas = ("Error 500: Erro interno no meu ego. Vou dar 'Ctrl+Z' na minha vida e fingir que não vi essa nota.", 
                 "Status 202: Essa nota demorou tanto para processar que parecia o Internet Explorer tentando carregar um GIF.", 
                 "Repensou na sua nota? Não? Mas mesmo assim eu agradeço a avaliação", 
                 "Fico feliz por ter avaliado bem, mas por que não um '5'?", 
                 "Agradeço pela sua nota 5, isso me ajuda muito a crescer e melhorar. Meu muito obrigado! ☺️")

    questionar = input(f'Gostaria de avaliar o sistema utilizado acima? (Responda apenas com S ou N)\n').lower()

    if questionar == 's':
        while True:
            try:
                avaliacao = int(input(f'Olá usúario, qual nota gostaria de estar dando para o código acima usado?\n'))

                if avaliacao == 3:
                    temporizador(3)
                    print(f'Sistema está reiniciando... Aguarde')

                if avaliacao >= 1 and avaliacao <= 5:
                    indice = avaliacao - 1
                    print(respostas[indice])
                    break

            except IndexError:
                print(f'Essa nota é inválida, por favor digite uma nota válida')
            except ValueError:
                print(f'Opa, isso é inválido, digite por favor uma nota válida')
    else:
        fim_bonito(f'Certo, não deseja avaliar, mas ficamos feliz por usar o nosso sistema')
