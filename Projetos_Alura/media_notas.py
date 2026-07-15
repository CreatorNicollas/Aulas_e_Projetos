from utilitarios import inicio_bonito, fim_bonito, sistema_avaliacao

# Sistema que visa calcular a média de notas dos alunos na escola

inicio_bonito(f'Olá seja bem vindo professor. Este sistema visa reduzir o tempo para calcular a média da notas de seus alunos, vamos começar?')

def calcula_media():
    aprovados = []
    reprovados = []

    nome_professor = input(f'Professor(a), poderia informar seu nome?\n')
    quantidade_alunos = int(input(f'{nome_professor}, poderia informar quantos alunos estão listados na sua matéria?\n'))

    for i in range(quantidade_alunos):
        nome_aluno = input(f'{nome_professor}, poderia informar o nome do aluno?\n')
        notas = input(f'{nome_professor}. Poderia informar as notas do {nome_aluno} para podermos calcular a média dele (Ah, mande elas separadas por vírgulas)?\n').split(', ')
        notas = [float(nota) for nota in notas]

        media = sum(notas) / len(notas)
        print(f'Aqui a média de notas do aluno: {media}\n')

        if media < 5:
            print(f'{nome_aluno}, foi reprovado na sua matéria\n')
            reprovados.append(nome_aluno)
        else:
            print(f'{nome_aluno} foi aprovado na sua matéria\n')
            aprovados.append(nome_aluno)

    print(f'Aqui está seus alunos aprovados: {', '.join(aprovados)}\n')
    print(f'Aqui está seus alunos reprovados: {', '.join(reprovados)}\n')

calcula_media()
fim_bonito(f'E aqui finalizamos esses sistema de calculo de notas, onde calculamos a media de notas de alunos de uma escola X (Não é a Escola do Professor Xaviver para crianças dotadas de superpoderes! Mas eu queria que fosse)')
sistema_avaliacao()