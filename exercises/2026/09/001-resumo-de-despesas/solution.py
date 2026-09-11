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
        gastos['por_categoria'][gasto['categoria']] = 0
        gastos['por_categoria'][gasto['categoria']] += gasto['valor_centavos'] 
    return gastos


