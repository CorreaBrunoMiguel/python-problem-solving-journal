# Código-base (assinatura e docstring) fornecido pelo assistente de IA.
# Implementação do corpo: aluno.


def conciliar_pagamentos(pedidos, pagamentos):
    """
    Concilia pedidos com seus pagamentos, usando valores em centavos.

    Args:
        pedidos: Lista de dicionários com pedido_id inteiro positivo único
            e valor_centavos inteiro positivo.
        pagamentos: Lista de dicionários com pedido_id inteiro positivo
            e valor_centavos inteiro não negativo. Cada registro conta
            como um pagamento, mesmo quando há registros idênticos.

    Returns:
        Dicionário com as chaves:
            pedidos: Lista ordenada por pedido_id, contendo um resumo por
                pedido com pedido_id, total_pago_centavos, saldo_centavos
                e situacao. O saldo é o valor do pedido menos o total pago.
                A situação é pendente para total zero, parcial para total
                positivo abaixo do valor, quitado para total igual ao valor
                e excedente para total acima do valor.
            pagamentos_orfaos: Lista crescente, sem repetições, dos IDs
                dos pagamentos que não correspondem a pedidos conhecidos.

        Sem pagamentos, o total de cada pedido é zero. Sem entradas,
        retorna {"pedidos": [], "pagamentos_orfaos": []}.

    Notes:
        As entradas são válidas e não devem ser modificadas.
        As estruturas retornadas devem ser independentes entre si e
        das entradas. Não há impressão nem acesso a recursos externos.
    """
    pass
