from utilitarios import inicio_bonito

inicio_bonito('Bem-vindo ao validador de CPF')
cpf = input('Digite seu CPF: ')

# Valindando seu CPF
def validar_cpf(cpf):

    if not cpf.isdigit():
        return 'Erro: O CPF deve conter apenas números.'
        
    if len(cpf) != 11:
        return 'Erro: O CPF deve ter exatamente 11 dígitos.'
    return 'CPF válido!'

print(validar_cpf(cpf))