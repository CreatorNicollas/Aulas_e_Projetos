from utilitarios import inicio_bonito, fim_bonito, subtitulos, sistema_avaliacao

# Arrumando uma lista de pedidos

inicio_bonito(f'Olá, vamos ajustar os pedidos solicitados aqui neste curto e simples programa')

lista_pedidos = []

def criar_pedido():
    
    pedido = input(f'Olá, seja bem vindo ao sistema automatizado de realização de pedidos, o que deseja comer hoje?\n').lower().split(', ')
    lista_pedidos.extend(pedido)
    print(f'Aqui está sua lista de pedidos {lista_pedidos}')

    confirmacao_pedidos = input(f'Sua lista de pedidos está correto para estarmos repassando para a cozinha? (Responda apenas com S ou N)').lower()

    while True:

        try:
            if confirmacao_pedidos == 's':
                subtitulos(f'Ok, seu pedido foi repassado para a cozinha e será entrgue em breve')
                break
            else:
                print(f'Certo, vamos prosseguir com a tratativa necessária...')
                
                resultado = corretor_pedidos()
                if resultado == "encerrar":
                    break

                confirmacao_pedidos = input(f'Sua lista atualizada é {lista_pedidos}. Está correta agora? (S/N): ').lower()

        except ValueError:
            print(f'Opa, isso não é válido, digite algo válido para prosseguirmos')

def corretor_pedidos():
    while True:
        validar_acao = input(f'O que deseja fazer? Adicionar(1), Remover(2), Substituir(3), Encerrar(4): ')
        
        if validar_acao == "1":
            incluir_item = input('Informe o item para adicionar: ').lower()
            lista_pedidos.append(incluir_item)
            print(f'Sua lista atualizada: {lista_pedidos}')
            break

        elif validar_acao == "2":
            excluir_item = input(f'Qual item deseja remover? ').lower()
            if excluir_item in lista_pedidos:
                lista_pedidos.remove(excluir_item)
                print(f'Removido! Lista atualizada: {lista_pedidos}')
            else:
                print("Item não encontrado no seu pedido.")
            break

        elif validar_acao == "3":
            substitui = input(f'Qual item será substituído? ').lower()
            if substitui in lista_pedidos:
                troca = input(f'Deseja trocar por qual item? ').lower()
                posicao = lista_pedidos.index(substitui)
                lista_pedidos.remove(substitui)
                lista_pedidos.insert(posicao, troca)
                print(f'Troca realizada! Lista atualizada: {lista_pedidos}')
            else:
                print("Item para substituição não encontrado.")
            break

        elif validar_acao == '4':
            print(f'Estamos encerrando por aqui, seu pedido ficou assim: {lista_pedidos}')
            return "encerrar"
            
        else:
            print("Opção inválida! Digite apenas 1, 2, 3 ou 4.")

criar_pedido()
fim_bonito(f'Aqui chegamos ao fim de mais um código onde eu transfomei algo simples em um bicho de sete cabeças que cospem fogo e ácido. Pois eu queria e quero testar meu aprendizado')
sistema_avaliacao()