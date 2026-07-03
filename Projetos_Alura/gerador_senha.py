from utilitarios import inicio_bonito, fim_bonito, temporizador
import random, string

# Gerador de senhas seguras

coleta_nome = input(f'Digite seu nome: ')
solicita_tempo = int(input(f'Aqui vou solicitar um tempo para gerar sua senha {coleta_nome}, pode digitar a seguir por favor(Em segundos): '))

def cria_senha():
    inicio_bonito(f'Venha gerar uma senha segura e aleatória para você, {coleta_nome}!')

    todos_caracteres = string.ascii_letters + string.digits + '!@#$%&*'

    senha = [
        random.choice(todos_caracteres)
    ]

    print(f'Estamos gerando sua senha, aguarde um momento Sr/Sra {coleta_nome}...')
    temporizador(solicita_tempo)

    senha.extend(random.choices(todos_caracteres, k=8))
    random.shuffle(senha)
    return ''.join(senha)

print(f'Aqui está a sua senha gerada Sr/Sra {coleta_nome}: {cria_senha()}')
fim_bonito('Programa encerrado! Por que o Dev não quer pensar muito em como fazer isso de uma melhor forma. Mas a senha gerada é segura e aleatória, pode confiar!')