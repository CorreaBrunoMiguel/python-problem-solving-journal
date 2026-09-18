# Revisão técnica assistida por IA — Desafio 005

Revisões serão acrescentadas preservando as anteriores. Este parecer distingue erros, melhorias e alternativas; não constitui certificação de domínio.

## Tentativa 01 — 18/09/2026

- **Commit:** [de0ac36](https://github.com/CorreaBrunoMiguel/python-problem-solving-journal/commit/de0ac366c54ba6dd9c291fc8a3d798959ad9749e).
- **Mensagem:** `feat: implementa tentativa 01 do desafio 005`.
- **Parecer:** nenhum erro funcional encontrado na inspeção e nos casos executados. Solução adequada ao contrato; testes e explicação serão trabalhados gradualmente.
- **Estado da avaliação:** em revisão. READMEs não alterados, conforme acordo de autorização específica.

### Execução e limites

Arquivos do commit executados em Python 3.12.14 no ambiente do assistente, sem alteração de lógica. Os **quatro asserts enviados passaram**, com saída vazia e código zero. Cobrem preservação das duas entradas, retorno completo do exemplo e retorno para dois inventários vazios.

O assistente executou cinco cenários adicionais, todos com comparação do retorno completo e preservação das duas entradas:

| Cenário | Resultado |
| --- | --- |
| Anterior vazio, atual preenchido, inclusive arquivo de zero bytes | Passou; somente adições, ordenadas |
| Atual vazio, anterior preenchido, inclusive zero bytes | Passou; somente remoções, ordenadas |
| Inventários idênticos com ordem de inserção diferente | Passou; três listas vazias |
| Aumento, redução e transições de/para zero | Passou; alterados em ordem alfabética |
| Nome antigo removido e novo adicionado, com mesmo tamanho | Passou; não inferiu renomeação |

Foi feita também uma verificação de independência: no resultado para dois inventários vazios, alterar adicionados não afetou removidos ou alterados; alterar removidos não afetou as outras listas. Passou.

Essas verificações adicionais são do assistente, não foram incorporadas ao código do aluno e não representam todos os testes possíveis.

### Acertos

- Usa pertinência de chaves para existência e comparação de valores para alteração, sem confundir arquivo vazio com arquivo ausente.
- Detecta aumento e redução com a mesma comparação de desigualdade.
- Percorre o inventário atual para adições/alterações e o anterior para remoções, sem modificar nenhum deles.
- Cria três listas distintas e ordena apenas a saída.
- Implementação curta, proporcional ao problema, com solução e testes separados.
- Os testes já incluem preservação de ambas as entradas e vazio na primeira entrega, retomando práticas trabalhadas anteriormente.

### Apontamentos

**Melhoria recomendada — cobertura:** falta teste do aluno para independência das listas. Os dois inventários vazios oferecem um ponto de partida simples: as três listas começam iguais em conteúdo, mas precisam ser objetos independentes. Trabalhar esse teste primeiro.

**Melhoria recomendada — cenários:** posteriormente, acrescentar casos com apenas um inventário vazio e com redução de tamanho. O exemplo só contém aumento para alterados e apenas um arquivo nessa lista, portanto não verifica a ordenação de múltiplos alterados. Os casos adicionais do assistente confirmam o comportamento atual, mas não substituem os testes do aluno.

**Alternativa opcional — legibilidade:** o else contendo somente outro if pode ser expresso com elif, reduzindo um nível de indentação. A estrutura atual é correta; não é necessário refatorar para concluir.

**Alternativa opcional — nomes:** `nome_arquivo` comunica melhor o conteúdo de `item`. Não há falha funcional no nome atual.

**Melhoria recomendada — mensagens:** as duas verificações de preservação usam a mesma mensagem. Identificar “inventário anterior” e “inventário atual” melhora o diagnóstico. Corrigir “da dicionário” para “do dicionário” é um ajuste editorial.

Deepcopy é válido; como os valores são inteiros imutáveis, cópias superficiais também bastariam. Não é preciso trocar essa escolha agora.

### Eficiência

Se n é a quantidade de arquivos anteriores, m a de atuais e a, r e c as quantidades de adicionados, removidos e alterados, o tempo esperado é O(n + m + a log a + r log r + c log c), com operações médias de dicionário e custos de chaves considerados constantes. Listas vazias ou unitárias não acrescentam custo relevante de ordenação.

O retorno ocupa O(a + r + c + 1). A ordenação pode usar memória auxiliar proporcional à lista ordenada. Não há justificativa para otimização adicional nesta etapa.

### Autoria e aprendizagem

Assinatura e docstring foram fornecidas pelo assistente no código-base. O comentário de autoria do código-base foi removido na entrega; a procedência continua explícita no README e fica registrada aqui. O corpo da implementação foi entregue pelo aluno; nenhuma solução completa foi fornecida nesta conversa.

O exemplo de entrada e o esperado vêm do enunciado. Há evidência de aplicação de testes já praticados, mas não se presume domínio independente de todos os comportamentos. Comparação entre inventários e construção de testes permanecem em progresso parcial, aguardando explicação e ampliação dirigida. A análise de complexidade acima é do assistente.

### Retomada

Próxima tarefa: testar a independência das listas retornadas a partir do resultado de `comparar_inventarios({}, {})`, acrescentando um nome a uma categoria e verificando que as outras permanecem vazias. O aluno escreverá e apresentará o trecho antes de outro commit.

As demais sugestões ficam registradas para avanço por etapas, sem cobrança simultânea. Nenhum código ou teste do aluno foi alterado.
