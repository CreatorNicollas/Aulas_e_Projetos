from utilitarios import inicio_bonito, fim_bonito, subtitulos, temporizador

# Lista de itens da despensa
inicio_bonito(f'Seja bem_vindo ao organizador de despensa')
organizador = input(f'Olá, como Sr(a) organizador(a) da despensa, qual seria seu nome? ')

def valida_despensa():
    despensa = ["arroz", "feijão", "macarrão", "leite", "ovos", "sal", "óleo", "açúcar"]
    lista_compras = []

    while True:

        mantimento = input(f'{organizador}, diga qual item você deseja saber se está em falta na despensa: ').lower()

        if mantimento not in despensa:
            print(f'{organizador},  precisamos comprar mais {mantimento} para a despensa.')
            adicionar_compra = input(f'{organizador}, deseja adicionar o {mantimento} à lista de compras? (S/N):').lower()
            if adicionar_compra == 's':
                lista_compras.append(mantimento)
                print(f'Item adicionado a lista de compras: \n', ', '.join(lista_compras))
            else:
                temporizador(10)
                subtitulos(f'{organizador}... O dinheiro tá curto? kkkkkk')
        else:
            print(f'{organizador}, não precisamos comprar {mantimento} para a despensa.')

        continuar = input(f'{organizador}, deseja continuar com a verificação da despensa? (S/N): ').lower()

        if continuar != 's':
            print(f'Ok, encerramos por aqui o serviço!')
            break
        else:
            print(f'Vamos manter a verificação da despensa, {organizador}!')
        
valida_despensa()
fim_bonito(f'Obrigado por utilizar o organizador de despensa, {organizador}. Você agora tem uma ideia das coisas que tem ou não em casa. Achou que ia ter uma piada do Dev aqui?')