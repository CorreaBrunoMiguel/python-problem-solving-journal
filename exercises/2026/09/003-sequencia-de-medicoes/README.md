# 003 — Sequência de medições

- **Início:** 11/09/2026
- **Estado:** pausado
- **Objetivo técnico:** identificar um trecho contínuo de crescimento em uma sequência, respeitando limites e desempate.
- **Autoria do enunciado:** assistente de IA.
- **Implementação e raciocínio:** abordagem discutida com orientação; implementação ainda não revisada.

## Problema

Um sensor registra medições na ordem em que elas acontecem. Precisamos localizar o maior trecho de medições consecutivas em que cada valor seja estritamente maior que o anterior.

Implemente:

```python
def maior_trecho_crescente(medicoes):
```

## Entrada

Uma lista de números inteiros, que podem ser negativos, zero ou positivos. A posição na lista representa a ordem temporal.

Um trecho é contínuo: não é permitido pular medições. Crescimento estrito significa que valores iguais interrompem o crescimento.

## Exemplo principal

Entrada:

```python
medicoes = [12, 15, 18, 14, 16, 20, 23, 19]
```

Retorno esperado:

```python
{"inicio": 3, "fim": 6, "tamanho": 4}
```

O trecho escolhido é `[14, 16, 20, 23]`. Começa no índice 3 e termina no índice 6, incluindo os dois extremos. O tamanho conta medições, não comparações.

## Requisitos

1. Retornar um dicionário com exatamente as chaves `inicio`, `fim` e `tamanho`.
2. Identificar o trecho contínuo estritamente crescente com mais medições.
3. Em caso de empate no tamanho, escolher o trecho que começa primeiro, isto é, com menor índice inicial.
4. Usar índices iniciados em zero. Tanto `inicio` quanto `fim` são inclusivos.
5. Uma única medição é um trecho válido de tamanho 1. Se nenhum par consecutivo crescer, o resultado deve apontar para a primeira medição.
6. Para uma lista vazia, retornar `{"inicio": None, "fim": None, "tamanho": 0}`.
7. Não modificar a lista recebida nem reordenar seus elementos.
8. Retornar o resultado; não imprimir dentro da função.

## Exemplos de interpretação

| Entrada | Retorno esperado | Motivo |
| --- | --- | --- |
| `[2, 4, 1, 3]` | `{"inicio": 0, "fim": 1, "tamanho": 2}` | Há empate; escolher o primeiro trecho. |
| `[5, 5, 5]` | `{"inicio": 0, "fim": 0, "tamanho": 1}` | Igualdade não é crescimento. |
| `[7]` | `{"inicio": 0, "fim": 0, "tamanho": 1}` | Uma medição é um trecho válido. |

## Restrições e escopo

- Todas as entradas respeitam o contrato; não validar tipos.
- Não é necessário ler arquivos, criar interface, usar input ou instalar bibliotecas externas.
- Não devolver a lista do trecho; devolver apenas os índices e seu tamanho.
- A escolha da abordagem é sua. Não há exigência de uma técnica específica ou de otimização nesta primeira tentativa.

## Implementação e verificação

Entregar `solution.py` e `test_solution.py`. Os testes devem importar a função e usar assert.

Escolha verificações que diferenciem os comportamentos do contrato, incluindo casos seus além dos exemplos. Comente brevemente o propósito de cada caso. Compare retornos completos e verifique a preservação da entrada.

Aplique quatro espaços por nível de indentação e nomes claros. Use a docstring para descrever o contrato com precisão.

Não é necessário criar um teste de independência de lista retornada: neste desafio, a saída não contém listas.

## Ambiente e execução

### Ambiente

- **Python de referência:** 3.12.7, informado pelo aluno no desafio 001. Atualizar se o ambiente utilizado mudar.
- **Dependências externas:** nenhuma.

### Arquivos da entrega

| Arquivo | Responsabilidade |
| --- | --- |
| `solution.py` | Implementação de `maior_trecho_crescente` |
| `test_solution.py` | Dados e verificações com assert |
| `REVIEW.md` | Criado pelo assistente após a primeira análise |

### Como executar os testes

Após criar os arquivos, a partir da raiz do repositório:

```bash
python exercises/2026/09/003-sequencia-de-medicoes/test_solution.py
```

Executar sem `-O`. Se todos os asserts executados passarem e não houver impressões, o comando terminará sem saída.

**Verificação atual:** nenhuma implementação recebida ou executada.

## Registro de tentativas e análise

Faça commit e push da tentativa para revisão. O assistente analisará correção, clareza, testes e decisões sem alterar sua implementação. As análises serão acrescentadas ao REVIEW.md, identificando o commit e o apoio recebido.

**Situação atual:** pausado a pedido do aluno; ponto de retomada registrado abaixo.

## Pausa e retomada

- **Data da pausa:** 16/09/2026.
- **Estado:** pausado.
- **Ponto atual:** construção da abordagem com `while` para identificar os trechos crescentes e selecionar o maior. O aluno propôs registrar os trechos e comparar seus tamanhos ao final.
- **Pendência:** organizar o avanço do índice e o encerramento dos trechos, incluindo o último, traduzindo o raciocínio em código.
- **Próxima ação:** percorrer manualmente uma lista curta e acompanhar índice, início e fim do trecho antes de retomar a implementação.
- **Situação da avaliação:** implementação ainda não revisada; a pausa não representa conclusão.

