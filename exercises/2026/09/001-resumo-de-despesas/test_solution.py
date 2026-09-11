from copy import deepcopy

from solution import resumir_despesas

sem_despesas = []

# total 10000, alimentacao: 4000, transporte: 2000, lazer: 4000
despesas_teste = [
    {"categoria": "alimentacao", "valor_centavos": 1000},
    {"categoria": "transporte", "valor_centavos": 2000},
    {"categoria": "alimentacao", "valor_centavos": 3000},
    {"categoria": "lazer", "valor_centavos": 4000},
    {"categoria": "educacao", "valor_centavos": 0}
]

# Testes
antes = deepcopy(despesas_teste)
obtido = resumir_despesas(despesas_teste)
assert despesas_teste == antes, "A função modifica a lista passada como argumento"
assert obtido['total_centavos'] == 10000, "Total calculado está errado"
assert obtido['por_categoria']['alimentacao'] == 4000, "Total dos gastos com alimentação está errado"
assert obtido['por_categoria']['transporte'] == 2000, "Total dos gastos com transporte está errado"
assert obtido['por_categoria']['lazer'] == 4000, "Total dos gastos com lazer está errado"
assert obtido["por_categoria"]['educacao'] == 0, "Total dos gastos com educacao está errado"
esperado = {"total_centavos": 10000, "por_categoria": {"alimentacao": 4000, "transporte": 2000, "lazer": 4000, "educacao": 0}}
assert esperado == obtido
obtido = resumir_despesas(sem_despesas)
assert obtido["total_centavos"] == 0
assert obtido['por_categoria'] == {}
