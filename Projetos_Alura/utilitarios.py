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
    os.system('cls')
    linha = '=' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()