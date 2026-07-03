from utilitarios import inicio_bonito, fim_bonito, temporizador

# Calculadora com tratativa de erros
inicio_bonito(f'Seja bem vindo a calculadora, cuidado para não ser banido')

def soma(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

def calculadora():
    try:
        num1 = float(input(f'Por favor digite o primeiro número: '))
        operacao = input(f'Por favor informe qual operação deseja realizar (+, -, *, /): ')
        num2 = float(input(f'Por favor digite o segundo número: '))

        if operacao == '+':
            resultado = soma(num1, num2)
        elif operacao == '-':
            resultado = subtrair(num1, num2)
        elif operacao == '*':
            resultado = multiplicar(num1, num2)
        elif operacao == '/':
            resultado = dividir(num1, num2)
        else:
            print(f'Operação inválida tente novamente')
            return
        
        print(f'Estamos fazendo as contas, em alguns segundos você obterá seu resultado...')
        temporizador(5)
        print(f'O resultado da sua conta está aqui: {resultado}')

    except ValueError:
        print(f'Por favor digite um número válido!')
    except ZeroDivisionError:
        print(f'Não realizamos divisão por zero, tente novamente')

calculadora()
fim_bonito(f'E aqui finalizamos essa calculadora onde você acaba de ser banido por tentar dividir por zero que sei, pois ao rodar esse código eu ganhei acesso a todos os dados do seu PC, você se achava mais esperto que eu não é? Mas obrigado por usar a calculadora, volte sempre!')
print(f'Eu esqueci que você foi banido daqui, crie uma conta nova e retorne aqui')