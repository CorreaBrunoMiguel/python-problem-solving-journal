def organizar_inscricoes(emails):
    """
    Recebe uma lista de emails (verificados)
    Retorna um dicionário com as chaves
        - inscritos: lista com emails únicos na ordem que aparecem
        - repetidas: numero de emails repetidos 1 ou mais vezes
    """
    
    resposta = {"inscritos": [], "repetidas": 0}
    
    for email in emails:
        if email not in resposta['inscritos']:
            resposta["inscritos"].append(email)
        else:
            resposta['repetidas'] += 1
        
    return resposta