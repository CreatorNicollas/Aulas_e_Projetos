import os, time

'''Este documento contém funções que são utilizadas para marcar horários, temporizar e embelezar os textos dos programas testes e outros.

Sistema Avaliativo irá passar por uma reestruturação futura, onde irá mostrar mais opções
'''

# Marcador de horário
def horario_inicial():
    '''
    Essa função é utilizada para marcar o horário inicial que o código comecou a rodar
    '''
    horario_atual = time.localtime()
    hora_formatada = time.strftime('%H:%M', horario_atual)

    print(f'Iniciando o programa às {hora_formatada} horas.')

def horario_final():
    '''
    Essa função é utilizada para marcar o horário final que o código terminou de rodar
    '''
    horario_atual = time.localtime()
    hora_formatada = time.strftime('%H:%M', horario_atual)

    print(f'Encerrando o programa às {hora_formatada} horas.')

# Temporizadores
def temporizador(tempo):
    '''
    Essa função é utilizada para fazer o código parar em pontos especificos por um tempo determinado

    O input dela é dado via o parametro "Tempo"
    '''
    time.sleep(tempo)

def barra_loading_temporizada(tempo, texto='Processando'):
    '''
    Essa função é utilizada para fazer o código parar em pontos especificos por um tempo determinado e gerar uma barra de carregamento seguida da mensagem pre definida

    O input dela é dado via o parametro "Tempo" seguindo o mesmo padrão de sua antecessora
    '''
    print(texto, end = '')
    passo = tempo / 10

    for _ in range(10):
        time.sleep(passo)
        print('.', end='', flush=True)
    
    print(' [CONCLUÍDO]\n')

# Embelezador de Textos
def inicio_bonito(texto):
    '''
    Formata e destaca o texto inicial em linhas delimitadoras.
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '-' * (len(texto) + 4)
    print(linha)
    print(f'| {texto} |')
    print(linha)
    horario_inicial()
    print()

def fim_bonito(texto):
    '''
    Formata e destaca o texto final em linhas delimitadoras.
    '''
    linha = '-' * (len(texto) + 4)
    print()
    horario_final()
    print(linha)
    print(f'| {texto} |')
    print(linha)

def subtitulos(texto):
    '''
    Formata e destaca subtítulos ou textos secundários com linhas delimitadoras.
    '''
    linha = '=' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

# Sistema de avaliação para os meus atuais e futuros sistemas

def sistema_avaliacao():
    '''
    Essa função é um sistema de avaliação desenvolvido para usúarios darem uma nota para o Dev que criou o sistema
    '''

    respostas = ("Error 500: Erro interno no meu ego. Vou dar 'Ctrl+Z' na minha vida e fingir que não vi essa nota.", 
                 "Status 202: Essa nota demorou tanto para processar que parecia o Internet Explorer tentando carregar um GIF.", 
                 "Repensou na sua nota? Não? Mas mesmo assim eu agradeço a avaliação", 
                 "Fico feliz por ter avaliado bem, mas por que não um '5'?", 
                 "Agradeço pela sua nota 5, isso me ajuda muito a crescer e melhorar. Meu muito obrigado! ☺️")

    questionar = input(f'Gostaria de avaliar o sistema utilizado acima? (Responda apenas com S ou N)\n').lower()

    if questionar == 's':
        while True:
                avaliacao = int(input(f'Olá usúario, qual nota gostaria de estar dando para o código acima usado?\n'))

                if avaliacao == 3:
                    barra_loading_temporizada(5, 'O sistema está reiniciando')

                if avaliacao >= 1 and avaliacao <= 5:
                    indice = avaliacao - 1
                    print(respostas[indice])
                    break
                else:
                    print(f'Por favor, digite uma nota entre 1 e 5')
    else:
        fim_bonito(f'Certo, não deseja avaliar, mas ficamos feliz por usar o nosso sistema')
