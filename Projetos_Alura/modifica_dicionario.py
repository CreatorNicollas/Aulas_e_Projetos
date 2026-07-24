from utilitarios import inicio_bonito, fim_bonito, subtitulos, sistema_avaliacao

# Sistema para modificação de um dicionario pre definido no sistema

inicio_bonito(f'Seja Bem vindo ao modificador de itens dentro do seu estoque!')

def modifica():
    estoque = {
        "Caderno universitário": 50, 

        "Caneta azul": 120, 

        "Borracha branca": 30 
    }

    produto = input('Diga-me qual produto irá atualizar: ')
    nova_quantidade = int(input(f'Qual é a nova quantidade desse produto: '))
    
    while True:
        if produto in estoque:
            estoque[produto] = nova_quantidade
            subtitulos(f'Quantidade atualizada com sucesso! {estoque}')
            break
        else:
            subtitulos(f'{produto} não encontrado no estoque. Revise por favor')

modifica()
fim_bonito(f'Aqui se encerra esse programa que futuramente se tornará um só com o que cria um dicionario com os itens passados.')
sistema_avaliacao()