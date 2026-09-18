# 006 — Conciliação de pedidos e pagamentos

- **Início:** 18/09/2026
- **Estado:** em andamento
- **Objetivo técnico:** relacionar duas fontes por identificador, acumular valores e classificar resultados.
- **Autoria do enunciado, exemplo, assinatura e docstring:** assistente de IA.
- **Implementação e asserts:** aluno, com orientação progressiva.

## Problema

No contexto fictício do FulfillOps, pedidos e pagamentos chegam em listas separadas. Um pedido pode receber vários pagamentos. Também podem chegar pagamentos com identificadores que não existem na lista de pedidos.

Implemente em `solution.py`:

```python
def conciliar_pagamentos(pedidos, pagamentos):
```

A função deve apresentar o total pago e a situação de cada pedido, além de identificar pagamentos sem pedido correspondente.

## Entrada

Duas listas de dicionários, com todas as entradas válidas:

- `pedidos`: registros com `pedido_id` (inteiro positivo único nessa lista) e `valor_centavos` (inteiro positivo).
- `pagamentos`: registros com `pedido_id` (inteiro positivo) e `valor_centavos` (inteiro maior ou igual a zero).

Valores monetários são inteiros em centavos, sem booleanos. Não use valores de ponto flutuante.

Um identificador pode aparecer várias vezes em pagamentos. Cada registro representa um pagamento distinto: mesmo dois registros idênticos devem ser contabilizados. As listas podem estar vazias e não estão necessariamente ordenadas.

## Retorno

Um dicionário com exatamente duas chaves:

- `pedidos`: lista de resumos, um para cada pedido de entrada, ordenada por `pedido_id` crescente.
- `pagamentos_orfaos`: lista dos identificadores presentes nos pagamentos, mas ausentes dos pedidos, sem repetição e em ordem crescente.

Cada resumo de pedido contém exatamente:

| Chave | Conteúdo |
| --- | --- |
| `pedido_id` | Identificador do pedido |
| `total_pago_centavos` | Soma de todos os pagamentos desse pedido; zero se não houver |
| `saldo_centavos` | Valor do pedido menos o total pago; negativo quando há excedente |
| `situacao` | Uma das quatro strings definidas abaixo |

### Situações

| Condição | Situação |
| --- | --- |
| Total pago igual a zero | `pendente` |
| Total pago maior que zero e menor que o valor do pedido | `parcial` |
| Total pago igual ao valor do pedido | `quitado` |
| Total pago maior que o valor do pedido | `excedente` |

Um pagamento de zero centavos não quita nem torna parcial um pedido. Pagamentos órfãos não entram nos totais de nenhum pedido conhecido.

## Exemplo

```python
pedidos = [
    {"pedido_id": 30, "valor_centavos": 1000},
    {"pedido_id": 10, "valor_centavos": 500},
    {"pedido_id": 40, "valor_centavos": 800},
    {"pedido_id": 20, "valor_centavos": 700},
]

pagamentos = [
    {"pedido_id": 30, "valor_centavos": 600},
    {"pedido_id": 99, "valor_centavos": 100},
    {"pedido_id": 10, "valor_centavos": 200},
    {"pedido_id": 20, "valor_centavos": 900},
    {"pedido_id": 30, "valor_centavos": 400},
    {"pedido_id": 40, "valor_centavos": 0},
    {"pedido_id": 99, "valor_centavos": 50},
]
```

Retorno esperado:

```python
{
    "pedidos": [
        {
            "pedido_id": 10,
            "total_pago_centavos": 200,
            "saldo_centavos": 300,
            "situacao": "parcial",
        },
        {
            "pedido_id": 20,
            "total_pago_centavos": 900,
            "saldo_centavos": -200,
            "situacao": "excedente",
        },
        {
            "pedido_id": 30,
            "total_pago_centavos": 1000,
            "saldo_centavos": 0,
            "situacao": "quitado",
        },
        {
            "pedido_id": 40,
            "total_pago_centavos": 0,
            "saldo_centavos": 800,
            "situacao": "pendente",
        },
    ],
    "pagamentos_orfaos": [99],
}
```

## Requisitos e limites

1. Incluir todos os pedidos conhecidos exatamente uma vez, mesmo sem pagamentos.
2. Somar todos os pagamentos de cada pedido, independentemente da posição dos registros.
3. Classificar usando o total acumulado e calcular o saldo com seu sinal.
4. Ordenar as duas listas de saída por identificador crescente; a ordem das chaves dos dicionários não é relevante.
5. Listar cada identificador órfão uma única vez, inclusive se seus pagamentos forem de zero centavos.
6. Para duas entradas vazias, retornar `{"pedidos": [], "pagamentos_orfaos": []}`.
7. Com pedidos vazios, listar apenas os identificadores órfãos. Com pagamentos vazios, todos os pedidos ficam pendentes.
8. Não modificar as listas nem os dicionários de entrada.
9. Criar estruturas de saída independentes: alterar um resumo não deve alterar outro nem as entradas. As duas listas de saída também devem ser distintas.
10. Retornar o resultado, sem imprimir na função.

Use apenas Python e sua biblioteca padrão. Não há acesso ao banco de dados, arquivos, APIs, validação de entradas, estornos, datas ou identificação de pagamentos duplicados. Não é obrigatório usar uma técnica específica; a clareza e o custo da abordagem serão discutidos na revisão.

## Entrega e testes

| Arquivo | Responsabilidade |
| --- | --- |
| `solution.py` | Código-base da IA com assinatura, docstring e `pass`; corpo implementado pelo aluno |
| `test_solution.py` | Entradas, chamadas e asserts; produzido pelo aluno com orientação |
| `REVIEW.md` | Criado pelo assistente após a entrega; preserva o histórico das análises |

Comece com a implementação e os testes que conseguir construir. Não é necessário entregar todos os cenários de uma vez.

Seguiremos o padrão combinado: o assistente identifica lacunas e fornece estruturas de entrada; o aluno prevê o retorno, escreve os asserts e executa as verificações. Asserções ficam em `test_solution.py`, separadas da solução. Comentários breves podem identificar a finalidade de cada caso.

Além do exemplo, a revisão trabalhará gradualmente entradas vazias, ausência de pagamentos, pagamentos repetidos, identificadores órfãos, ordenação e independência das estruturas. Não são exigidas novas ferramentas de testes.

## Ambiente e execução

- **Python de referência:** 3.12.7, informado pelo aluno.
- **Dependências externas:** nenhuma.
- **Formatação:** configuração Ruff existente no projeto.

Após criar os testes, execute da raiz, sem `-O`:

```bash
python exercises/2026/09/006-conciliacao-de-pagamentos/test_solution.py
```

Se todos os asserts passarem e não houver prints, a execução terminará sem saída.

## Acompanhamento

**Situação atual:** enunciado e código-base publicados; aguardando primeira tentativa. O código-base com `pass` ainda não implementa o contrato.

As revisões distinguirão autoria, orientação recebida, inspeção e execução. Atualizações dos READMEs dependem de autorização. O D005 está concluído e o D003 permanece pausado.
