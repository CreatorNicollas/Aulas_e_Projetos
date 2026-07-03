from utilitarios import inicio_bonito, fim_bonito, subtitulos
import os

afazeres = []

def exibir_opcoes():
    inicio_bonito('Seja bem-vindo ao Gereciador de tarefas')

    print('1. Adicionar tarefas')
    print('2. Visualizar tarefas')
    print('3. Remover tarefas')
    print('4. Sair')

def voltar_inicio():
    input(f'Aperte qualquer tecla para retorno ao menu inicial')
    main()

def opcao_invalida():
    print(f'Opção escolhida inexistente, escolha uma válida!')
    voltar_inicio()

def adicionar_tarefas():
    subtitulos(f'Adicionando novas Tarefas em sua agenda')
    tarefa = input(f'Informe a tarefa a ser adicionada a lista de afazeres: ')
    afazeres.append(tarefa)
    print('\n'.join(afazeres))
    voltar_inicio()

def visualizar_tarefas():
    subtitulos('Aqui estão suas tarefas pedentes em ordem de adição: ')
    for indice, tarefa in enumerate(afazeres, start=1):
        print(f'{indice}. {tarefa}')
    voltar_inicio()

def remover_tarefas():
    subtitulos('Remoção de tarefas está pronto')
    print('\n'.join(afazeres))

    remocao_item = input('Qual tarefa deseja remover? ')
    
    if remocao_item in afazeres:
        afazeres.remove(remocao_item)
        print(f'Item {remocao_item} foi retirado da lista')
    else:
        print(f'Erro: O {remocao_item} não existe na lista de afazeres')

    print(f'A sua lista de afazeres está assim:')
    print('\n'.join(afazeres))
    voltar_inicio()

def sair():
    subtitulos(f'Fechando sua lista de afazeres...')

def escolher_opcao():

    try:
        opcao_escolhida = int(input('Por favor digite a opção escolhida: '))

        if opcao_escolhida == 1:
            adicionar_tarefas()
        elif opcao_escolhida == 2:
            visualizar_tarefas()
        elif opcao_escolhida == 3:
            remover_tarefas()
        elif opcao_escolhida == 4:
            sair()
        else:
            opcao_invalida()
    except:
        print('Opção inválida, por favor digite uma opção válida')

def main():
    os.system('cls')
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

fim_bonito(f'Aqui finalizamos sua lista de afazeres, onde você poderá controlar suas tarefas diárias, semanais e mensais (Isso se aqui salvasse todas as coisas após essa mensagem, diga adeus para tudo que tentou até aqui, mas no futuro eu irei fazer isso aqui funcional =) )')