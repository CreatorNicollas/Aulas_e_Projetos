from utilitarios import inicio_bonito, fim_bonito, subtitulos

# Lista de voluntários de uma ONG

inicio_bonito(f'Olá! Seja Bem-vindo a lista de voluntários da nossa ONG, Instituto Recomeço Animal ')

def lista_voluntarios():
    voluntarios = []

    while True:
        nome = input(f'Por favor, diga-me os nomes dos voluntários que desejam ajudar nossa ONG (Para encerrar a lista digite "sair"): \n')

        if nome.lower() == 'sair':
                subtitulos(f'Você optou por sair da lista de voluntários. Agradecemos sua participação!')
                print(f'A lista de voluntários cadastrados ficou asssim:\n{", ".join(voluntarios)}')
                fim_bonito(f'Obrigado por ajudar nossa causa e lembre-se: "Ajudar um animal é ajudar a salvar uma vida de 4 patas!" O que? Aqui não tem piadas sobre eu ser um péssimo Dev e sim sobre a causa animal.')
                break

        voluntarios.append(nome)

        print(f'Voluntário(a) {nome} adicionado(a) à lista de voluntários! Ficamos muito lisonjeados com sua ajuda na nossa causa animal! 🐶🐱')
        
lista_voluntarios()