# 004 — Cobertura de indicadores

- **Início:** 16/09/2026
- **Estado:** concluído
- **Conclusão:** 16/09/2026
- **Objetivo técnico:** agrupar registros por país e distinguir valores disponíveis de ausentes.
- **Autoria do enunciado:** assistente de IA.
- **Implementação:** entregue e revisada; explicações do aluno e apoio recebido registrados no [REVIEW.md](REVIEW.md).

## Problema

Antes de comparar um indicador entre países, precisamos verificar quais observações têm valor e quais estão ausentes.

Você recebe registros de um único indicador em diferentes países e anos. Produza um resumo por país com a quantidade de valores disponíveis, a quantidade de valores ausentes e os anos associados às ausências.

O contexto se inspira no diagnóstico de cobertura de dados por país. Os dados do exemplo são fictícios; não representam estatísticas oficiais.

Implemente:

```python
def resumir_cobertura(registros):
```

## Entrada

Uma lista de dicionários com estas chaves:

| Chave | Conteúdo |
| --- | --- |
| `pais` | Código de país como string não vazia, já padronizada |
| `ano` | Inteiro positivo |
| `valor` | Número inteiro ou float finito, ou `None` |

Regras da entrada:

- Há apenas um indicador no conjunto.
- Não há repetição da combinação país/ano.
- Os registros podem estar em qualquer ordem e misturar países.
- Os valores numéricos podem ser positivos, negativos ou zero. Não haverá booleanos, NaN ou infinito.
- Todas as entradas respeitam o contrato; não é necessário validar tipos ou campos.

## Exemplo

Entrada:

```python
registros = [
    {"pais": "BRA", "ano": 2023, "valor": None},
    {"pais": "ARG", "ano": 2022, "valor": 0},
    {"pais": "BRA", "ano": 2021, "valor": 12.5},
    {"pais": "URY", "ano": 2023, "valor": None},
    {"pais": "BRA", "ano": 2020, "valor": None},
    {"pais": "ARG", "ano": 2021, "valor": -2.3},
]
```

Retorno esperado:

```python
{
    "BRA": {
        "disponiveis": 1,
        "ausentes": 2,
        "anos_ausentes": [2020, 2023],
    },
    "ARG": {
        "disponiveis": 2,
        "ausentes": 0,
        "anos_ausentes": [],
    },
    "URY": {
        "disponiveis": 0,
        "ausentes": 1,
        "anos_ausentes": [2023],
    },
}
```

## Requisitos

1. Retornar um dicionário com uma entrada para cada país presente nos registros, sem acrescentar outros países.
2. Cada país deve ter exatamente as chaves `disponiveis`, `ausentes` e `anos_ausentes`.
3. `disponiveis` conta registros cujo valor é numérico. Zero e números negativos são valores disponíveis.
4. `ausentes` conta registros cujo valor é `None`. Apenas `None` representa ausência neste contrato.
5. `anos_ausentes` contém os anos dos registros com valor ausente, em ordem crescente.
6. Incluir países com todos os valores ausentes e países sem nenhuma ausência. Neste último caso, `anos_ausentes` será uma lista vazia.
7. Para uma lista de entrada vazia, retornar `{}`.
8. Não modificar a lista recebida nem os dicionários de entrada.
9. Os resumos e as listas de anos de países diferentes devem ser independentes: alterar o resumo de um país no retorno não deve alterar o de outro.
10. Retornar o resultado; não imprimir dentro da função.

A ordem das chaves de países no dicionário não importa. A ordem dos anos dentro de cada lista importa.

**Limite importante:** analisar apenas os registros recebidos. Um ano não informado não deve ser inferido como ausente. No exemplo, BRA não tem registro de 2022, mas esse ano não entra na contagem nem na lista de ausências. Não existe intervalo de anos obrigatório neste desafio.

## Restrições e escopo

- Usar Python sem bibliotecas externas, Pandas, leitura de CSV, APIs ou banco de dados.
- Não calcular médias, percentuais, ranking ou preencher valores ausentes.
- Não normalizar códigos de países nem validar conhecimento geográfico.
- A escolha das estruturas e da abordagem é sua; não é exigida técnica específica.

## Implementação e verificação

Entregar `solution.py` e `test_solution.py`. Os testes devem importar a função e usar `assert`.

Escolha casos além do exemplo para verificar as regras, com comentários curtos sobre a finalidade de cada um. Compare o retorno completo, verifique a preservação da entrada e a independência dos resumos por país.

Use nomes claros, docstring coerente com o contrato e a configuração Ruff adotada no repositório. Não é necessário introduzir framework de testes.

## Ambiente e execução

### Ambiente

- **Python de referência:** 3.12.7, informado pelo aluno no desafio 001. Atualizar se o ambiente utilizado mudar.
- **Dependências externas da solução:** nenhuma.

### Arquivos da entrega

| Arquivo | Responsabilidade |
| --- | --- |
| `solution.py` | Implementação de `resumir_cobertura` |
| `test_solution.py` | Dados e verificações com `assert` |
| `REVIEW.md` | Criado pelo assistente após a primeira análise |

### Como executar os testes

Após criar os arquivos, a partir da raiz do repositório:

```bash
python exercises/2026/09/004-cobertura-de-indicadores/test_solution.py
```

Executar sem `-O`. Se todos os asserts executados passarem e não houver impressões, o comando terminará sem saída.

**Verificação atual:** os quatro asserts da entrega final (`8ce1446`) passaram no ambiente do assistente (Python 3.12.14), assim como uma verificação adicional direcionada a zero inteiro, zero float, negativo, positivo e None. Resultados e limites no [REVIEW.md](REVIEW.md).

## Registro de tentativas e análise

Faça commit e push da tentativa para revisão. O assistente analisará correção, clareza, testes e decisões sem alterar sua implementação. As revisões serão acrescentadas ao REVIEW.md, identificando o commit e o apoio recebido.

**Situação atual:** concluído após revisão do commit `8ce1446`. Requisitos essenciais atendidos, com orientação na construção dos testes e na refatoração. A docstring foi fornecida pelo assistente. Conclusão não equivale a domínio consolidado; consulte o [REVIEW.md](REVIEW.md). O desafio 003 permanece pausado.
