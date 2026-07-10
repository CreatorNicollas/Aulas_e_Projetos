from utilitarios import inicio_bonito, fim_bonito, subtitulos, sistema_avaliacao

# Organizando ordem de apresentação de evento

inicio_bonito(f'Vamos organizar uma lista de eventos hoje neste programa, não de TV e sim de computador')

def organizador_evento():

    eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']
    eventos_registrados.reverse()
    subtitulos(f'Aqui está de forma organizada: {eventos_registrados}')

organizador_evento()
fim_bonito(f'Aqui chegamos ao fim desse programa, onde organizamos lista de uma forma que fica na ordem que os eventos')
sistema_avaliacao()