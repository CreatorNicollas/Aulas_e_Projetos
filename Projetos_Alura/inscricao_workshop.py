from utilitarios import inicio_bonito, fim_bonito, subtitulos, sistema_avaliacao

# Gerenciamento de inscrição de um Workshop que eu não sei o que é, apenas me pediram para criar uma sistema para isso!

inicio_bonito(f'Seja Bem vindo ao gerenciador de inscrição do seu Workshop!')

participantes = {
    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 
}

remover_desistencia = input(f'Poderia por favor informar o nome do aluno que veio a desistir do projeto:\n')

for workshop, nomes in participantes.items():
    nomes.discard(remover_desistencia)

print('Lista atualizada de participantes:')

for workshop, nomes in participantes.items():
    subtitulos(f'- {workshop}: {nomes}')

fim_bonito(f'Aqui encerramos mais um código simples pois dessa vez resolvi não me prolongar demais nesse código por pura preguiça e com isso vou deixar apenas isso aí. =]')
sistema_avaliacao()