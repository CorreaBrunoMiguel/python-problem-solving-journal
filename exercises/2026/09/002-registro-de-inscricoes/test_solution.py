from solution import organizar_inscricoes
from copy import deepcopy

emails_repetidos = [
    "carla@example.com",
    "ana@example.com",
    "eduardo@example.com",
    "bruno@example.com",
    "ana@example.com",
    "fernanda@example.com",
    "carla@example.com",
    "bruno@example.com",
    "ana@example.com",
]

sem_email = []

emails_unicos = [
    "marcos@example.com",
    "ana@example.com",
    "zuleica@example.com",
    "bruno@example.com",
    "fernanda@example.com",
    "carlos@example.com",
]

# Teste email repetidos
antes = deepcopy(emails_repetidos)
obtido = organizar_inscricoes(emails_repetidos)
assert antes == emails_repetidos, "Função modifica argumento inplace"
assert obtido['inscritos'] == [
    "carla@example.com",
    "ana@example.com",
    "eduardo@example.com",
    "bruno@example.com",
    "fernanda@example.com"
], "A função não retorna a lista de emails correta ou na ordem errada"
assert obtido['inscritos'][0] == 'carla@example.com', "Retornou primeiro inscrito incorreto"
assert obtido['inscritos'][-1] == 'fernanda@example.com', "Retornou último inscrito incorreto"
assert obtido['repetidas'] == 4, 'Calculou errado  número de emails repetidos'
assert obtido == {
    "inscritos": [
        "carla@example.com",
        "ana@example.com",
        "eduardo@example.com",
        "bruno@example.com",
        "fernanda@example.com"
],
    "repetidas": 4,
}, "Retornou o objeto errado"

# Teste sem emails
obtido = organizar_inscricoes(sem_email)
assert obtido == {"inscritos": [], "repetidas": 0}, "Retornou objeto padrão vazio errado"
assert obtido["inscritos"] == [], "Não retornou lista vazia"
assert obtido["repetidas"] == 0, "Calculou número diferente de zero para entrada nula"

# Teste email únicos
antes = deepcopy(emails_unicos)
obtido = organizar_inscricoes(emails_unicos)
assert obtido['inscritos'] == [
    "marcos@example.com",
    "ana@example.com",
    "zuleica@example.com",
    "bruno@example.com",
    "fernanda@example.com",
    "carlos@example.com"
], "Modificou a ordem ou os emails"
assert obtido['repetidas'] == 0, "Lista não possui email repetidos"
assert obtido == {
    "inscritos": [
        "marcos@example.com",
        "ana@example.com",
        "zuleica@example.com",
        "bruno@example.com",
        "fernanda@example.com",
        "carlos@example.com",
],
    "repetidas": 0
}
obtido["inscritos"].append('leo@example.com')
assert antes == emails_unicos, "Modificou referência"
