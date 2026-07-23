from utilitarios import inicio_bonito, fim_bonito, subtitulos, sistema_avaliacao

# Neste códigos vamos unificar e comparar conjuntos

inicio_bonito(f'Sejam bem vindos ao unificador e comparador de conjuntos. Está pronto para fazer isso?')

nome_user = input(f'Poderia informar seu nome por favor?\n')

def comparador():
    equipe_1 = {"planejar reunião", "revisar documento", "testar sistema"}
    equipe_2 = {"testar sistema", "implementar funcionalidade", "corrigir bug"}

    combinador_de_tarefas = equipe_1.union(equipe_2)

    remocao = input(f'{nome_user}, deseja remover alguma tarefa? (Responda com S ou N)\n')

    if remocao == 's':
        remover_tarefas = input(f'{nome_user}. Quais tarefas deseja remover?\n').lower()
        subtitulos(f'{nome_user}, aqui está as tarefas finais para ambas as equipes: {combinador_de_tarefas}')
    
        if remover_tarefas in combinador_de_tarefas:
            combinador_de_tarefas.remove(remover_tarefas)
    else:
        subtitulos(f'{nome_user}, aqui está as tarefas finais para ambas as equipes: {combinador_de_tarefas}')

comparador()
fim_bonito(f'E esse é meu código desse desafio, fico feliz por ter usado ele, se quiser testar os outros e avaliar eles e este aqui, ficaria muito feliz')
sistema_avaliacao()