# 002 — Registro de inscrições

- **Início:** 11/09/2026
- **Estado:** em revisão
- **Objetivo técnico:** identificar inscrições repetidas e preservar a ordem de chegada das inscrições únicas.
- **Autoria do enunciado:** assistente de IA.
- **Implementação:** primeira tentativa entregue; explicação do raciocínio pendente.

## Problema

Uma oficina recebe inscrições por e-mail. Uma pessoa pode enviar sua inscrição mais de uma vez. A organização precisa obter a lista de inscritos sem repetições, mantendo a ordem em que cada e-mail apareceu pela primeira vez, e saber quantos envios repetidos recebeu.

Implemente:

```python
def organizar_inscricoes(emails):
```

## Entrada

Uma lista de strings. Cada string representa um e-mail.

Os e-mails já estão padronizados em letras minúsculas, sem espaços nas extremidades. Considere duas inscrições da mesma pessoa apenas quando as strings forem iguais. Não é necessário validar o formato dos e-mails.

## Exemplo

Entrada:

```python
emails = [
    "ana@example.com",
    "bruno@example.com",
    "ana@example.com",
    "carla@example.com",
    "bruno@example.com",
    "ana@example.com",
]
```

Retorno esperado:

```python
{
    "inscritos": [
        "ana@example.com",
        "bruno@example.com",
        "carla@example.com",
    ],
    "repetidas": 3,
}
```

Há três envios repetidos: o segundo envio de Ana, o segundo de Bruno e o terceiro de Ana. Não se está contando apenas quantas pessoas repetiram a inscrição.

## Requisitos

1. Retornar um dicionário com exatamente as chaves `inscritos` e `repetidas`.
2. `inscritos` deve ser uma lista contendo cada e-mail uma única vez.
3. Manter a ordem da primeira ocorrência de cada e-mail. Não ordenar alfabeticamente.
4. `repetidas` deve ser um inteiro que conte cada ocorrência posterior à primeira de um mesmo e-mail.
5. Para a lista vazia, retornar `{"inscritos": [], "repetidas": 0}`.
6. Não modificar a lista recebida.
7. A lista retornada em `inscritos` deve ser um novo objeto, inclusive quando não houver repetições: modificar essa lista depois não deve modificar a entrada.
8. Retornar o resultado; não imprimir dentro da função.

## Restrições e escopo

- Todas as entradas respeitam o contrato.
- Não tratar diferenças de maiúsculas, espaços ou aliases de e-mail.
- Usar recursos nativos do Python, sem bibliotecas externas.
- Não é necessário ler arquivos, criar interface ou usar `input()`.
- A escolha das estruturas de dados é sua. Não há exigência de uma técnica específica.

## Implementação e verificação

Entregar `solution.py` e `test_solution.py`. Os testes devem importar a função e usar `assert`.

Escolha casos que verifiquem os requisitos e explique brevemente a finalidade de cada um, com comentários junto dos testes. Inclua comparação do retorno completo e verificação da preservação da entrada. Considere também a independência da lista retornada.

A ordem dos elementos de uma lista importa na comparação de igualdade.

Aplique quatro espaços por nível de indentação, retomando o acordo adiado no desafio 001. Priorize nomes claros e uma solução proporcional ao problema.

## Ambiente e execução

### Ambiente

- **Python de referência:** 3.12.7, informado pelo aluno no desafio 001. Confirmar ou atualizar se o ambiente utilizado mudar.
- **Dependências externas:** nenhuma.

### Arquivos da entrega

| Arquivo | Responsabilidade |
| --- | --- |
| `solution.py` | Implementação de `organizar_inscricoes` |
| `test_solution.py` | Dados e verificações com `assert` |
| `REVIEW.md` | Criado pelo assistente após a primeira análise |

### Como executar os testes

Após criar os arquivos, a partir da raiz do repositório:

```bash
python exercises/2026/09/002-registro-de-inscricoes/test_solution.py
```

Executar sem `-O`. Se todos os asserts executados passarem e não houver impressões, o comando terminará sem saída.

**Verificação atual:** nove asserts enviados e quatro casos adicionais do assistente passaram em Python 3.12.14 no commit `c56717a`. Veja limites e detalhes no [REVIEW.md](REVIEW.md).

## Registro de tentativas e análise

Faça commit e push da tentativa para revisão. O assistente analisará correção, clareza, testes, boas práticas e custos pertinentes, sem alterar sua implementação.

As revisões serão acrescentadas a `REVIEW.md`, com o commit analisado e o apoio recebido. Registre justificativas reais; não é necessário produzir um relatório extenso.

**Situação atual:** tentativa 01 analisada, sem erro funcional encontrado. Em revisão para explicação da abordagem e ampliação dos testes de ordem e independência da saída. Consulte o [REVIEW.md](REVIEW.md).
