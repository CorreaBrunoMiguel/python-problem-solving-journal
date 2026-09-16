from copy import deepcopy

from solution import resumir_cobertura

registros = [
    {"pais": "BRA", "ano": 2023, "valor": None},
    {"pais": "ARG", "ano": 2022, "valor": 0},
    {"pais": "BRA", "ano": 2021, "valor": 12.5},
    {"pais": "URY", "ano": 2023, "valor": None},
    {"pais": "BRA", "ano": 2020, "valor": None},
    {"pais": "ARG", "ano": 2021, "valor": -2.3},
]

antes = registros
original = deepcopy(registros)
resposta = resumir_cobertura(registros)

assert registros == original, "A função modificou o conteúdo da lista recebida."

assert resposta == {
    "BRA": {
        "disponiveis": 1,
        "ausentes": 2,
        "anos_ausentes": [2020, 2023],
    },
    "ARG": {
        "disponiveis": 2,
        "ausentes": 0,
        "anos_ausentes": [],
    },
    "URY": {
        "disponiveis": 0,
        "ausentes": 1,
        "anos_ausentes": [2023],
    },
}

arg_antes = deepcopy(resposta["ARG"])
resposta["BRA"]["anos_ausentes"].append(2026)
assert resposta["ARG"] == arg_antes

resposta = resumir_cobertura([])
assert resposta == {}
