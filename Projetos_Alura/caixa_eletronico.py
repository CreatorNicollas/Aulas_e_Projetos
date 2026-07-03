from utilitarios import inicio_bonito, fim_bonito, subtitulos

# Simulando um caixa eletrônico
inicio_bonito(f'Seja bem-vindo ao simulador de ciaxa de eletrônico')

coleta_nome = input(f'Olá cliente, poderia informar seu nome: ')
cpf = input('Digite seu CPF: ')


def validar_cpf(cpf):

    if not cpf.isdigit():
        return 'Erro: O CPF deve conter apenas números.'
        
    if len(cpf) != 11:
        return 'Erro: O CPF deve ter exatamente 11 dígitos.'
    return 'CPF válido!'

def caixa_eletronico():
    cedulas = [100, 50, 20, 10, 5, 2]

    if cpf == 'CPF válido':
        print('Podemos seguir com os atendimento')
    else:
        validar_cpf(cpf)

    try:
        subtitulos(f'Olá {coleta_nome}, que bom te ter por aqui novamente')

        valor = int(input(f'{coleta_nome} qual o valor que deseja sacar? '))

        if valor <= 0:
            print('Erro: O valor deve ser positivo.')
        elif valor % 2 != 0:
            print('Erro: O valor deve ser múltiplo de 2.')
        else:
            print('Cédulas entregues:')

            for cedula in cedulas:
                quantidade = valor // cedula
                if quantidade > 0:
                    print(f'{quantidade} cédulas de R$ {cedula}')
                    valor = valor % cedula
    except ValueError:
        print('Erro: Digite um valor númerico válido.')

caixa_eletronico()
fim_bonito(f'{coleta_nome}. Espero que você não tenha fornecido dados reais nesse código pois ele salva tudo na nuvem e lá todos conseguem ver, fora que salvo no meu computador e depois eu faço uma negociação com a PF para pegar devedores igual a você caloteiro. Fique esperto não viu? Caloteiro')