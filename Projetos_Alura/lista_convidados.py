from utilitarios import inicio_bonito, fim_bonito, subtitulos, sistema_avaliacao

inicio_bonito(f'Olá organziador(a) do evento. Do que irá se tratar esse evento de hoje?')

# Organizador de lista de convidados

def lista_convidados():
    convidados = []
    
    criar_lista = input("Deseja iniciar uma lista de convidados? (S/N): ").lower()
    
    if criar_lista != 's':
        print("Certo, então não teremos eventos por esses dias...")
        fim_bonito("E então aqui encerramos esse programa por enquanto. Volte sempre!")
        sistema_avaliacao()
        return

    while True:
        convidado = input("\nDigite o nome do convidado que deseja adicionar: ")
        
        if not convidados:
            print("Como a lista está vazia, este convidado ficará automaticamente na posição 1.")
            posicao_convidado = 1
        else:
            try:
                posicao_convidado = int(input(f"Em qual posição (de 1 a {len(convidados) + 1}) ele irá ficar? "))
            except ValueError:
                print("Por favor, digite um número válido!")
                continue

        convidados.insert(posicao_convidado - 1, convidado)
        print(f"A lista de convidados atualizada ficou assim: {convidados}")

        pausa = input("\nDeseja adicionar mais alguém à lista? (S/N): ").lower()
        if pausa != 's':
            fim_bonito("A lista foi concluida e impressa para para você agradecemos o uso!")
            sistema_avaliacao()
            break

lista_convidados()