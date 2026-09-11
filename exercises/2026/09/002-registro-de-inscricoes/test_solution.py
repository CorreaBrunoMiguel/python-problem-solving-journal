from solution import organizar_inscricoes
from copy import deepcopy

emails = [
    "ana@example.com",
    "bruno@example.com",
    "ana@example.com",
    "carla@example.com",
    "bruno@example.com",
    "ana@example.com",
]

sem_email = []

antes = deepcopy(emails)
obtido = organizar_inscricoes(emails)

# Testar integridade do lista
assert antes == emails, "Função modifica argumento inplace"
# Testar resultados unitários
assert obtido['inscritos'] == [
        "ana@example.com",
        "bruno@example.com",
        "carla@example.com",
    ], "A função não retorna a lista de emails correta ou na ordem errada"
assert obtido['inscritos'][0] == 'ana@example.com', "Retornou primeiro inscrito incorreto"
assert obtido['inscritos'][-1] == 'carla@example.com', "Retornou último inscrito incorreto"
assert obtido['repetidas'] == 3, 'Calculou errado  número de emails repetidos'
# Testar para objeto inteiro
assert obtido == {
    "inscritos": [
        "ana@example.com",
        "bruno@example.com",
        "carla@example.com",
    ],
    "repetidas": 3,
}, "Retornou o objeto errado"
obtido = organizar_inscricoes(sem_email)
assert obtido == {"inscritos": [], "repetidas": 0}, "Retornou objeto padrão vazio errado"
assert obtido["inscritos"] == [], "Não retornou lista vazia"
assert obtido["repetidas"] == 0, "Calculou número diferente de zero para entrada nula"