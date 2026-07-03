from utilitarios import inicio_bonito, fim_bonito

inicio_bonito('Seja bem-vindo ao Contador de Vogais!')
texto = input(f'Digite o texto aqui: ').lower()

# Contador de Vogais
def contar_vogais(texto):
    
    vogais = 'aeiouAEIOU'
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    contador_V = 0
    contador_C = 0

    for vogal in vogais:

        if vogal in texto:
            contador_V += 1

    for consoante in consoantes:

        if consoante in texto:
            contador_C += 1

    print(f'O número de vogais no texto é de: {contador_V}')
    print(f'O número de consoantes no texto é de: {contador_C}')

contar_vogais(texto)

fim_bonito('É isso que este programa faz. Daqui em dia o Dev ficou com preguiça de fazer alguma coisa, então encerra aqui =)')