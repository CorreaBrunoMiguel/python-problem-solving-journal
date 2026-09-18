from copy import deepcopy

from solution import comparar_inventarios

anterior = {
    "populacao.csv": 800,
    "notas.txt": 0,
    "renda.csv": 1200,
    "legado.csv": 450,
}

atual = {
    "saude.csv": 900,
    "renda.csv": 1350,
    "notas.txt": 0,
    "educacao.csv": 700,
}

anterior_original = deepcopy(anterior)
atual_original = deepcopy(atual)

resposta = comparar_inventarios(anterior, atual)

assert atual_original == atual, "A função modificou o conteúdo da dicionário recebido."
assert anterior_original == anterior, (
    "A função modificou o conteúdo da dicionário recebido."
)

assert resposta == {
    "adicionados": ["educacao.csv", "saude.csv"],
    "removidos": ["legado.csv", "populacao.csv"],
    "alterados": ["renda.csv"],
}, "Função retorna objeto diferente do esperado"

resposta = comparar_inventarios({}, {})

assert resposta == {"adicionados": [], "removidos": [], "alterados": []}, (
    "Função não retorna o objeto correto ao receber dois dicionários vazios"
)
