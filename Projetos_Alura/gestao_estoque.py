from utilitarios import inicio_bonito, fim_bonito, subtitulos, sistema_avaliacao

inicio_bonito(f'Olá gerenciador. Vamos organizar este estoque hoje?')

# Organizador do estoque

def organizacao():
    estoque1 = tuple(input(f'Por favor informe o que temos dentro do primeiro estoque (Separe eles por vírgulas): ').split(', '))
    estoque2 = tuple(input(f'Por favor informe o que temos dentro do segundo estoque (Separe eles por vírgulas): ').split(', '))

    estoque_juntos = estoque1 + estoque2

    subtitulos(f'Aqui a lista de forma de geral do que temos no estoque do comércio: {estoque_juntos}.')

organizacao()
fim_bonito(f'E é só isso que esse código faz, agradeço se avaliar com uma nota 5 após o uso de sistema que está em melhoria constante')
sistema_avaliacao()