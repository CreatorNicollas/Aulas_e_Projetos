from utilitarios import inicio_bonito, fim_bonito, subtitulos, sistema_avaliacao

# Sistema onde analisa o valor da venda de mercadorias

inicio_bonito('Bem vindo ao sistema de analise de vendas de produtos gerais')

vendas = {
    'Eletrônicos': [
        {'produto': 'Smartphone', 'quantidade': 5, 'valor_unitario': 2000},
        {'produto': 'Tablet', 'quantidade': 3, 'valor_unitario': 1500}
    ],
    'Eletrodoméstico': [
        {'produto': 'Geladeira', 'quantidade': 2, 'valor_unitario': 3000},
        {'produto': 'Micro-ondas', 'quantidade': 4, 'valor_unitario': 800}
    ],
    'Livros': [
        {'produto': 'Livro A', 'quantidade': 10, 'valor_unitario': 50},
        {'produto': 'Livro B', 'quantidade': 6, 'valor_unitario': 100}
    ]
}

subtitulos('Total de vendas por categoria:')

for categoria, itens in vendas.items():
    total = 0

    for item in itens:
        total += item['quantidade'] * item['valor_unitario']

    print(f'- {categoria}: R$ {total:.2f}')