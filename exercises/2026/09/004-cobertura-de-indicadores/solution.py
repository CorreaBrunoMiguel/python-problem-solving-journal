def resumir_cobertura(registros):
    """
    Resume a disponibilidade de valores de um indicador por país.

    Args:
        registros: Lista de dicionários com as chaves "pais", "ano" e
            "valor", sem repetição de país/ano. O valor pode ser um
            número finito ou None.

    Returns:
        Dicionário por país com:
            - disponiveis: quantidade de registros com valor numérico.
            - ausentes: quantidade de registros com valor None.
            - anos_ausentes: anos com valor None, em ordem crescente.

        Retorna um dicionário vazio para uma entrada vazia.

    Notes:
        Zero e números negativos são valores disponíveis.
        Anos sem registro não são considerados ausentes.
        Não há intervalo temporal obrigatório.
        A entrada não é modificada, e os resumos de países diferentes
        são independentes.
    """
    resposta = {}

    for registro in registros:
        pais = registro["pais"]
        ano = registro["ano"]
        valor = registro["valor"]
        if pais not in resposta:
            resposta[pais] = {"disponiveis": 0, "ausentes": 0, "anos_ausentes": []}
        if valor is not None:
            resposta[pais]["disponiveis"] += 1
        else:
            resposta[pais]["ausentes"] += 1
            resposta[pais]["anos_ausentes"].append(ano)

    for resumo in resposta.values():
        resumo["anos_ausentes"].sort()

    return resposta
