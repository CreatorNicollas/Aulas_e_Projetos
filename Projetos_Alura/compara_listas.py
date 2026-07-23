from utilitarios import inicio_bonito, fim_bonito, subtitulos, sistema_avaliacao

# Neste sistema comparamos duas listas diferentes e diremos o que tem em uma que a outra não possui

inicio_bonito(f'Neste código vamos comparar listas e te mostrar o que cada uma tem em comum e de diferente!')

def comparador_de_listas():

    lista1 = set(input(f'Por favor informe a primeira lista:\n').lower().split(', '))
    lista2 = set(input(f'Por favor informe a segunda lista:\n').lower().split(', '))

    comuns = lista1.intersection(lista2)
    exclusivos_lista1 = lista1.difference(lista2)
    exclusivos_lista2 = lista2.difference(lista1)

    resultados = {
        'Palavras em comum': comuns,
        'Exclusivas da Lista 1':
        exclusivos_lista1,
        'Exclusivas da Lista 2': exclusivos_lista2
    }

    for titulo, conjunto in resultados.items():
        conteudo = ', '.join(conjunto) if conjunto else 'Nenhum item encontrado'
        subtitulos(f'{titulo}: {conteudo}')

comparador_de_listas()
fim_bonito(f'E por fim esse é o código que criamos até aqui, onde podemos ver suas listas organizadas e seus respectivos itens que tem ou não em comum')
sistema_avaliacao()