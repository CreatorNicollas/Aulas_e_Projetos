from utilitarios import inicio_bonito, fim_bonito, subtitulos

# Neste código irá definir permissões dependendo do cargo

inicio_bonito(f'Sejam Bem vindos ao sistema que irá dar suas permissões dependendo do seu cargo!')

def permissao():

    nome = input(f'Olá, poderia infromar seu nome?\n')
    #cargo = input(f'{nome}, poderia informar seu cargo?').lower()

    permissoes_principais = set(p.strip() for p in input(f'{nome}, poderia informar suas permissões principais: ').lower().split(','))
    permissoes_solicitadas = set(p.strip() for p in input(f'{nome}, poderia informar quais permissões deseja: ').lower().split(','))

    eh_subconjunto = permissoes_solicitadas.issubset(permissoes_principais)

    if eh_subconjunto:
        subtitulos("As permissões solicitadas fazem parte das permissões principais.")
    else:
        subtitulos("As permissões solicitadas não fazem parte das permissões principais.")

permissao()
fim_bonito(f'Sistema simples e sem avaliação pois isso aqui foi confuso demais para mim e é apenas isso o código. Recomendo olhar o "utilitarios.py" temos bastante coisas lá!')