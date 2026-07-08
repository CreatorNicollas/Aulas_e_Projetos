from utilitarios import inicio_bonito, fim_bonito, subtitulos

# Organizador de notas de um concurso

inicio_bonito(f'Sejam Bem-vindos todos ao organizador de notas deste concurso!')


def organiza_notas():
    nome_organizador = input(f'Jurado, poderia informar seu nome para registrarmos as notas do concurso? ')
    notas = input(f'Jurado {nome_organizador}, por favor insira as notas dos participantes separadas por vírgula: ').split(',')

    notas_finais = []

    for nota in notas:
        try:
            nota = float(nota.strip())
            notas_finais.append(nota)
        except ValueError:
            subtitulos(f'Erro: A nota "{nota}" não é válida. Por favor, insira apenas números separados por vírgulas.')

    notas_finais.sort()
    print(f'E as notas finais organizadas são: {notas_finais}')

organiza_notas()
fim_bonito(f'Aqui encerramos a organização das suas notas do concurso, agora me diga, era um concurso de que? Pois se for de desenvolvimento de programas, eu nem sei onde eu estou. Mas se for de quem passa mais tempo jogando...🎮')

'''
notas = [85, 70, 90, 60, 75]
print("Notas originais:", notas)

notas.sort()
print("Notas ordenadas:", notas)
'''