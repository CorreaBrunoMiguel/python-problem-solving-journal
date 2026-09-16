# 005 — Comparação de inventários

- **Início:** 16/09/2026
- **Estado:** em andamento
- **Objetivo técnico:** comparar presença e valores de chaves entre dois dicionários.
- **Autoria do enunciado e código-base:** assistente de IA.
- **Implementação e testes:** a serem produzidos pelo aluno.

## Problema

Um processo de atualização de dados mantém um inventário de arquivos antes e depois de cada execução. Compare os dois inventários para identificar arquivos adicionados, removidos e alterados.

Neste exercício, um inventário é um dicionário em que cada chave é um nome de arquivo e cada valor é seu tamanho em bytes. Os dados são fictícios; nenhum arquivo real precisa ser acessado.

Implemente em solution.py:

```python
def comparar_inventarios(anterior, atual):
```

## Entrada

Dois dicionários:

- `anterior`: inventário antes da atualização;
- `atual`: inventário depois da atualização.

As chaves são strings não vazias com nomes em letras minúsculas, caracteres ASCII e sem espaços nas extremidades. Os valores são inteiros maiores ou iguais a zero, sem booleanos. Zero representa um arquivo existente e vazio.

Todas as entradas são válidas. Nomes são comparados exatamente como recebidos, sem normalização. Dicionários podem estar vazios e sua ordem de inserção não tem significado.

## Exemplo

```python
anterior = {
    "populacao.csv": 800,
    "notas.txt": 0,
    "renda.csv": 1200,
    "legado.csv": 450,
}

atual = {
    "saude.csv": 900,
    "renda.csv": 1350,
    "notas.txt": 0,
    "educacao.csv": 700,
}
```

Retorno esperado:

```python
{
    "adicionados": ["educacao.csv", "saude.csv"],
    "removidos": ["legado.csv", "populacao.csv"],
    "alterados": ["renda.csv"],
}
```

`notas.txt` existe nos dois inventários com o mesmo tamanho, portanto não aparece no retorno.

## Requisitos

1. Retornar um dicionário com exatamente as chaves `adicionados`, `removidos` e `alterados`, sempre associadas a listas de nomes.
2. Adicionados existem somente em `atual`.
3. Removidos existem somente em `anterior`.
4. Alterados existem nos dois inventários, mas têm tamanhos diferentes, seja aumento ou redução.
5. Arquivos com o mesmo nome e tamanho não aparecem em nenhuma lista.
6. Cada lista deve estar em ordem alfabética crescente (ordem lexicográfica padrão do Python), sem repetições. Um arquivo não pode pertencer a mais de uma categoria.
7. Quando uma categoria não tiver arquivos, retornar sua lista vazia. Se os dois inventários forem vazios, retornar `{"adicionados": [], "removidos": [], "alterados": []}`.
8. Não modificar os dicionários de entrada.
9. As três listas de saída devem ser independentes: alterar uma não deve alterar as outras.
10. Retornar o resultado; não imprimir dentro da função.

**Limites da comparação:** tamanho igual é considerado ausência de alteração neste contrato, mesmo que arquivos reais pudessem ter conteúdos diferentes. Uma troca de nome será observada como remoção do nome antigo e adição do novo; não detectar renomeações.

## Escopo

- Python sem bibliotecas externas, leitura de diretórios, acesso a arquivos ou cálculo de hashes.
- Não validar tipos, calcular totais de bytes ou produzir relatórios adicionais.
- A abordagem e as estruturas auxiliares são suas escolhas. Não há técnica obrigatória.

## Entrega e verificação

| Arquivo | Responsabilidade |
| --- | --- |
| `solution.py` | Assinatura, docstring e pass fornecidos pela IA; implementar o corpo |
| `test_solution.py` | Casos e asserts produzidos pelo aluno |
| `REVIEW.md` | Análises do assistente após as entregas |

O código-base não implementa o contrato: pass é apenas um marcador provisório.

Comece com os testes que conseguir construir. Compare o retorno completo com o esperado e procure casos além do exemplo. Comente brevemente a finalidade dos testes. A preservação das duas entradas e a independência das listas fazem parte do contrato.

Conforme o acordo atual, as lacunas serão discutidas uma por vez no review. Não é necessário entregar uma suíte exaustiva na primeira tentativa.

Use a configuração Ruff do projeto e nomes que expressem o papel dos dados.

## Ambiente e execução

### Ambiente

- **Python de referência:** 3.12.7, informado pelo aluno anteriormente. Informar se mudar.
- **Dependências externas da solução:** nenhuma.

### Como executar os testes

Após criar test_solution.py, execute a partir da raiz:

```bash
python exercises/2026/09/005-comparacao-de-inventarios/test_solution.py
```

Execute sem `-O`. Se todos os asserts executados passarem e não houver prints, o comando terminará sem saída.

**Verificação atual:** apenas código-base fornecido; nenhuma solução implementada ou avaliada.

## Acompanhamento

As análises preservarão as tentativas no histórico e distinguirão implementação do aluno, código-base e orientação recebida. Alterações nos READMEs dependem de autorização.

**Situação atual:** aguardando primeira tentativa. O desafio 003 permanece pausado.
