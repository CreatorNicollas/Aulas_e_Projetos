from utilitarios import inicio_bonito

# Calculando Gorjetas
def calculando_gorjeta():
    inicio_bonito('Bem-vindo a calculadora de gorjetas!')
    print(f'Neste restaurante nossa sugestão de gorjeta é de 10%, mas você pode escolher o valor que desejar.\n')
    valor_conta = float(input(f'Digite o valor da conta: '))
    porcentagem_gorjeta = float(input(f'Digite o porcentagem de gorjeta: '))

    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    total_a_pagar = valor_conta + gorjeta

    print(f'O valor da gorjeta: R$ {gorjeta:.2f}')
    print(f'Total a pagar: R$ {total_a_pagar:.2f}')

calculando_gorjeta()