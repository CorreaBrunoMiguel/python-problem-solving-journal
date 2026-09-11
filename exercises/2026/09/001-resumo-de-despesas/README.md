# 001 — Resumo de despesas

- **Início:** 11/09/2026
- **Estado:** em revisão
- **Objetivo técnico:** transformar registros de despesas em um resumo consistente.
- **Autoria do enunciado:** assistente de IA.
- **Implementação:** primeira tentativa entregue pelo aluno; explicação do raciocínio pendente.

## Problema

Um sistema registra despesas individualmente. Uma mesma categoria pode aparecer várias vezes. Precisamos descobrir quanto foi gasto em cada categoria e no total.

Implemente uma função com este contrato:

```python
def resumir_despesas(despesas):
```

## Entrada

Uma lista de dicionários. Cada registro contém:

- `categoria`: texto não vazio;
- `valor_centavos`: número inteiro maior ou igual a zero.

Os valores representam centavos inteiros: `1250` corresponde a R$ 12,50. Todos os cálculos e resultados devem permanecer em centavos.

## Exemplo

Entrada:

```python
despesas = [
    {"categoria": "alimentacao", "valor_centavos": 1250},
    {"categoria": "transporte", "valor_centavos": 500},
    {"categoria": "alimentacao", "valor_centavos": 750},
]
```

Retorno esperado:

```python
{
    "total_centavos": 2500,
    "por_categoria": {
        "alimentacao": 2000,
        "transporte": 500,
    },
}
```

## Requisitos

1. Somar todas as despesas em `total_centavos`.
2. Apresentar em `por_categoria` a soma correspondente a cada categoria encontrada.
3. Para uma lista vazia, retornar `{"total_centavos": 0, "por_categoria": {}}`.
4. Preservar categorias cujo total seja zero.
5. Não modificar a lista recebida nem seus dicionários.
6. Retornar o resultado; imprimir não substitui o retorno.

## Restrições e escopo

- Todas as entradas respeitam o contrato; não é necessário validar tipos, campos ausentes ou valores negativos.
- Os nomes das categorias já estão padronizados.
- A ordem das categorias no resultado não importa.
- Usar apenas recursos nativos do Python, sem bibliotecas externas.
- Não é necessário criar interface, ler arquivos ou receber dados com `input()`.

## Implementação e verificação

O aluno escolhe o formato da tentativa (script ou notebook), preservando o contrato da função.

Além do exemplo fornecido, deve escolher casos de verificação e explicar o que cada um verifica. Pode usar `assert`. Um arquivo separado de testes deve ser criado apenas quando houver testes implementados.

Registrar a versão do Python efetivamente utilizada e as instruções de execução ao acrescentar a implementação.

## Ambiente e execução

### Ambiente

- **Python utilizado pelo aluno:** 3.12.7, informado pela saída de `python --version`.
- **Dependências externas:** nenhuma.

### Arquivos da entrega

Para a reorganização desta entrega em script, usar:

| Arquivo | Responsabilidade |
| --- | --- |
| `solution.py` | Implementação da função `resumir_despesas` |
| `test_solution.py` | Dados de teste e verificações com `assert`, importando a função de `solution.py` |
| `REVIEW.md` | Análises do assistente vinculadas às tentativas |

A nomenclatura acima é o padrão acordado para a próxima entrega; a tentativa 01 foi analisada com o arquivo `001_resumo_despesas.py`.

### Como executar os testes

Após organizar os arquivos conforme o padrão acima, a partir da raiz do repositório:

```bash
python exercises/2026/09/001-resumo-de-despesas/test_solution.py
```

Executar os asserts em modo normal, sem a opção `-O`.

Se todos os asserts executados passarem e não houver impressões, o comando terminará sem saída. Uma condição falsa em um assert produzirá `AssertionError`. A ausência de falhas vale para os casos efetivamente verificados; não comprova cobertura completa.

**Verificação desta reorganização:** pendente de envio e análise. Este comando documenta a execução prevista para os arquivos acordados.

## Registro de tentativas e análise

Cada tentativa será preservada por commit. Após commit e push do aluno, o assistente analisará os requisitos atendidos, erros, acertos, verificações e justificativas, sem alterar a solução.

As análises ficam em [REVIEW.md](REVIEW.md), identificadas como avaliações do assistente e vinculadas ao commit examinado. Reflexões e justificativas do aluno serão registradas apenas quando fornecidas por ele.

Se o aluno decidir revisar a implementação, a nova tentativa será registrada em outro commit no mesmo arquivo. Requisitos essenciais pendentes mantêm o exercício aberto.

**Situação atual:** tentativa 01 (`fe39594`) analisada. Nenhum erro funcional encontrado nos casos verificados. Em revisão para discussão das decisões e dos testes. Consulte o [parecer técnico](REVIEW.md).
