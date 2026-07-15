from utilitarios import inicio_bonito, fim_bonito, subtitulos, sistema_avaliacao

# Corrigindo posicionamento e nomes em uma lista

inicio_bonito(f'Vamos corrigir uma lista onde você colocou um nome errado')

def correcao():

    resultados = ["Ana", "Carlos", "Pedro"]
    print(f'Lista original: ', resultados)

    erro = input(f'Digite o nome diferente: ')
    
    if erro in resultados:
        correto = input(f'Digite o nome que está correto: ')
        posicao = resultados.index(erro)

        resultados.remove(erro)
        resultados.insert(posicao, correto)
        print(f'O nome {erro} que estava errado foi substituido pelo {correto} o qual se encontra correto')
        subtitulos(f'Lista atualizada: {resultados}')
    else:
        print(f'Nome não encontrado.')

correcao()
fim_bonito(f'Aqui finalizamos esse código que não faz demais pois ele tem uma funcionalidade muito especifica que é arrumar uma lista com um nome errado. Futuramemte terá alguma forma de montar isso de forma melhor')
sistema_avaliacao()