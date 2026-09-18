# 005 — Comparação de inventários

- **Início:** 16/09/2026
- **Estado:** concluído
- **Conclusão:** 18/09/2026
- **Objetivo técnico:** comparar presença e valores de chaves entre dois dicionários.
- **Autoria do enunciado e código-base:** assistente de IA.
- **Implementação:** aluno, sobre assinatura e docstring fornecidas pela IA.
- **Testes:** aluno, com orientação e entradas adicionais fornecidas pela IA.
- **Revisões:** [histórico de análise técnica](REVIEW.md).

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
| `solution.py` | Corpo implementado pelo aluno; assinatura e docstring fornecidas pela IA |
| `test_solution.py` | Asserts produzidos pelo aluno, com orientação na escolha de cenários e entradas |
| `REVIEW.md` | Análises do assistente após as entregas |

O código-base inicial continha `pass` como marcador provisório; o aluno o substituiu pela implementação.

Comece com os testes que conseguir construir. Compare o retorno completo com o esperado e procure casos além do exemplo. Comente brevemente a finalidade dos testes. A preservação das duas entradas e a independência das listas fazem parte do contrato.

Conforme o acordo atual, as lacunas serão discutidas uma por vez no review. Não é necessário entregar uma suíte exaustiva na primeira tentativa.

Use a configuração Ruff do projeto e nomes que expressem o papel dos dados.

## Ambiente e execução

### Ambiente

- **Python de referência:** 3.12.7, informado pelo aluno anteriormente. Informar se mudar.
- **Dependências externas da solução:** nenhuma.

### Como executar os testes

Execute a partir da raiz:

```bash
python exercises/2026/09/005-comparacao-de-inventarios/test_solution.py
```

Execute sem `-O`. Se todos os asserts executados passarem e não houver prints, o comando terminará sem saída.

**Verificação atual:** os nove asserts da entrega [5cf115e](https://github.com/CorreaBrunoMiguel/python-problem-solving-journal/commit/5cf115e6b6ed1fc73b5b4efd8e2dd60fc836e687) passaram no ambiente do assistente, com Python 3.12.14. Cenários adicionais executados na primeira revisão e limites da verificação estão registrados no [REVIEW.md](REVIEW.md).

## Acompanhamento

As análises preservarão as tentativas no histórico e distinguirão implementação do aluno, código-base e orientação recebida. Alterações nos READMEs dependem de autorização.

### Registro de conclusão — 18/09/2026

- Primeira implementação avaliada sem erro funcional encontrado.
- Testes ampliados progressivamente para cobrir independência das listas, um inventário vazio, zero bytes, aumento, redução e ordenação de múltiplos alterados.
- Na verificação de compreensão, o aluno explicou que percorrer apenas `atual` não permite encontrar arquivos removidos, pois esses nomes só estão em `anterior`.
- Implementação, testes e explicação aprovados para o escopo deste desafio. Melhorias opcionais permanecem no histórico de revisão.
- Padrão combinado para os testes: o assistente identifica lacunas e fornece entradas; o aluno prevê a saída, escreve os asserts e executa as verificações.

**Situação atual:** concluído. O desafio 003 permanece pausado.
