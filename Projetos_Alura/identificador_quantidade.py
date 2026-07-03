from utilitarios import inicio_bonito, fim_bonito

inicio_bonito(f'Bem-vindo ao Identificador de Quantidade!')
texto = input(f'Digite o texto o qual iremos identificar as palavras longas: ')

# Identificador de Palavras Longas
def identificador_palavras_longas(texto):
    texto = texto.split()

    lista_palavras_longas = []

    for palavra in texto:

        if len(palavra) > 10:
            lista_palavras_longas.append(palavra)

    if lista_palavras_longas:
            print(f'Palavras longas encontradas a seguir: ')
            for palavra in lista_palavras_longas:
                print(f'- {palavra}')
    else:
        print(f'Não há palavras longas no texto!')

identificador_palavras_longas(texto)
fim_bonito(f'O Dev cansou e fez isso aqui em 30 minutos, faça bom uso =)')