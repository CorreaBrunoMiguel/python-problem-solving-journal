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

resposta["adicionados"].append("teste.csv")
assert resposta["removidos"] == []
assert resposta["alterados"] == []

anterior = {"teste1.csv": 0, "teste2.csv": 100}
atual = {}

resposta = comparar_inventarios(anterior, atual)

assert resposta == {
    "adicionados": [],
    "removidos": ["teste1.csv", "teste2.csv"],
    "alterados": [],
}, "Função retorna objeto diferente do esperado"

anterior = {}
atual = {"super.csv": 0, "novo.csv": 200}

resposta = comparar_inventarios(anterior, atual)

assert resposta == {
    "adicionados": ["novo.csv", "super.csv"],
    "removidos": [],
    "alterados": [],
}, "Função retorna objeto diferente do esperado"

anterior = {
    "vendas.csv": 500,
    "clientes.csv": 200,
}

atual = {
    "vendas.csv": 300,
    "clientes.csv": 450,
}

resposta = comparar_inventarios(anterior, atual)

assert resposta == {
    "adicionados": [],
    "removidos": [],
    "alterados": ["clientes.csv", "vendas.csv"],
}, "Função retorna objeto diferente do esperado"
