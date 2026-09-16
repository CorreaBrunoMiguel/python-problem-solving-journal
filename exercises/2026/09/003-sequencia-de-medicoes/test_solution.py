# Teste com estrutura definida para facilitar assert
# Esperando aceitação do analisador

casos = [
    # 1. Maior sequência no início
    (
        [120, 480, 950, 1730, 4200, 3100, 3350, 3900, 800, 1450, 1450, 2200],
        {"inicio": 0, "fim": 4, "tamanho": 5},
    ),

    # 2. Maior sequência no meio
    (
        [8500, 3200, 4100, 6700, 9900, 15400, 23100, 1200, 5100, 8900, 3000, 7400],
        {"inicio": 1, "fim": 6, "tamanho": 6},
    ),

    # 3. Maior sequência no fim
    (
        [14000, 9200, 11000, 7600, 8100, 4300, 6700, 12500, 19800, 27400, 35100, 49000],
        {"inicio": 5, "fim": 11, "tamanho": 7},
    ),

    # 4. Lista inteira crescente
    (
        [150, 780, 2100, 4600, 9100, 15700, 23800, 35100, 49700, 68000, 90500],
        {"inicio": 0, "fim": 10, "tamanho": 11},
    ),

    # 5. Nenhum crescimento consecutivo
    (
        [92000, 81000, 81000, 65000, 47000, 31000, 31000, 18000, 9500, 4200],
        {"inicio": 0, "fim": 0, "tamanho": 1},
    ),
]