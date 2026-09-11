# Lista de despesas

despesas = [
    {"categoria": "alimentacao", "valor_centavos": 4590},
    {"categoria": "transporte", "valor_centavos": 1875},
    {"categoria": "moradia", "valor_centavos": 125000},
    {"categoria": "lazer", "valor_centavos": 3200},
    {"categoria": "alimentacao", "valor_centavos": 6890},
    {"categoria": "transporte", "valor_centavos": 2450},
    {"categoria": "lazer", "valor_centavos": 5500},
    {"categoria": "moradia", "valor_centavos": 18990},
    {"categoria": "alimentacao", "valor_centavos": 3745},
]

sem_despesas = []


# total 10000, alimentacao: 4000, transporte: 2000, lazer: 4000
despesas_teste = [
    {"categoria": "alimentacao", "valor_centavos": 1000},
    {"categoria": "transporte", "valor_centavos": 2000},
    {"categoria": "alimentacao", "valor_centavos": 3000},
    {"categoria": "lazer", "valor_centavos": 4000},
]


# Função do Desafio

def resumir_despesas(despesas):
  """
  Receber uma lista de dicionários com as despesas
  Cada dicionário terá 2 chaves: categoria e valor centavos
  Categoria: categoria da despesa um valor str
  Valor centavos: um inteiro que representa a quantidade de centavos
  Retornar dicionário com total dos gastos, e por categoria
  """
  gastos = {"total_centavos": 0, "por_categoria": {}}
  
  for gasto in despesas:
    gastos['total_centavos'] += gasto['valor_centavos']
    if gasto['categoria'] in gastos['por_categoria']:
      gastos['por_categoria'][gasto['categoria']] += gasto['valor_centavos']
    else:
      gastos['por_categoria'][gasto['categoria']] = gasto['valor_centavos'] 
  return gastos

# Testes
teste = resumir_despesas(despesas_teste)
assert teste['total_centavos'] == 10000, "Total calculado está errado"
assert teste['por_categoria']['alimentacao'] == 4000, "Total dos gastos com alimentação está errado"
assert teste['por_categoria']['transporte'] == 2000, "Total dos gastos com transporte está errado"
assert teste['por_categoria']['lazer'] == 4000, "Total dos gastos com lazer está errado"

ENTRADAS = [despesas, sem_despesas]

for entrada in ENTRADAS:
  print(resumir_despesas(entrada))
