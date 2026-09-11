# Revisão técnica assistida por IA — Desafio 002

As revisões serão acrescentadas preservando as anteriores. A análise distingue correção, melhorias recomendadas e alternativas opcionais; não constitui certificação de domínio.

## Tentativa 01 — 11/09/2026

- **Commit:** [c56717a](https://github.com/CorreaBrunoMiguel/python-problem-solving-journal/commit/c56717af1635a1dbc1ca93d33194774a61af3f42).
- **Mensagem:** `feat: implementa tentativa 01 do desafio 002`.
- **Estado:** em revisão.
- **Parecer:** nenhum erro funcional encontrado na inspeção e nos casos executados. Permanecem lacunas na cobertura dos testes e explicação das escolhas.

### Verificações executadas

Ambiente do assistente: **Python 3.12.14**. Arquivos do commit executados sem mudanças de lógica. O script de testes terminou sem saída e com código zero: **nove asserts passaram**.

O aluno verificou o exemplo do enunciado e a entrada vazia, incluindo preservação da entrada preenchida e igualdade do retorno completo. O total de asserts não equivale à quantidade de cenários distintos.

O assistente executou quatro casos adicionais:

| Caso | Resultado esperado resumido | Resultado |
| --- | --- | --- |
| Vazio | Lista vazia; zero repetidas | Passou |
| Todos únicos em ordem z, a, m | Preservar z, a, m; zero repetidas | Passou |
| Quatro ocorrências do mesmo e-mail | Um inscrito; três repetidas | Passou |
| Repetições intercaladas em ordem não alfabética | Preservar primeiras ocorrências; duas repetidas | Passou |

Para cada caso adicional, foram verificados retorno completo, preservação da entrada, identidade distinta da lista retornada e preservação da entrada após acrescentar um item à saída.

Os casos adicionais são de autoria do assistente, não foram adicionados aos arquivos do aluno e não representam cobertura exaustiva.

### Acertos e evolução

- A implementação adiciona cada e-mail apenas na primeira ocorrência e incrementa repetidas nas ocorrências posteriores. Isso atende à contagem de envios, não apenas de pessoas.
- A lista de saída é criada dentro da função e recebe elementos na ordem da leitura, sem modificar a entrada.
- O resultado inicial atende ao caso vazio.
- A solução é curta, legível, separada dos testes e não acrescenta funcionalidades fora do contrato.
- A indentação dos blocos da função agora respeita quatro espaços por nível, atendendo ao acordo do desafio 001.
- Preservação com deepcopy e comparação do retorno completo já aparecem na primeira tentativa do 002. Há transferência do que foi trabalhado no 001.

### Apontamentos

| Classificação | Evidência e consequência | Orientação |
| --- | --- | --- |
| Melhoria recomendada — cobertura | O assert de preservação apenas compara a entrada antes e depois da chamada; não verifica o requisito de saída independente. Uma função poderia devolver a própria entrada sem alterá-la durante a chamada. | Incluir uma verificação que diferencie essas duas propriedades, especialmente no caso sem repetição. |
| Melhoria recomendada — cobertura | Os primeiros e-mails distintos do exemplo já estão em ordem alfabética. Uma implementação que ordenasse a saída também passaria nesse caso. | Escolher um caso cuja ordem de chegada seja diferente da ordem alfabética. |
| Melhoria recomendada — precisão | A docstring descreve repetidas como “numero de emails repetidos 1 ou mais vezes”, o que pode ser entendido como quantidade de e-mails distintos repetidos. | Explicitar que conta ocorrências posteriores à primeira. O código já faz a contagem correta. |
| Melhoria recomendada — terminologia | Uma mensagem chama a lista vazia de “entrada nula”. | Usar “lista vazia”: `[]` e `None` são entradas diferentes; None está fora do contrato. |
| Melhoria recomendada — estilo, baixa prioridade | Import local antes do import da biblioteca padrão; espaços finais e ausência de quebra de linha ao final dos arquivos. | Organizar imports com biblioteca padrão antes dos locais e finalizar arquivos com newline. Não são erros funcionais nem exigem ferramentas novas. |
| Alternativa opcional — concisão dos testes | Primeiro e último inscritos já estão cobertos pela igualdade da lista; os campos vazios também são cobertos pela igualdade completa. | Manter verificações específicas se ajudarem no diagnóstico, mas priorizar novos cenários em vez de repetir verificações equivalentes. |
| Alternativa opcional — cópia | deepcopy é correto, mas a entrada é uma lista de strings imutáveis. | Uma cópia superficial da lista seria suficiente neste contrato. Não é necessário alterar o teste atual. |

### Eficiência

Se **n** é o número de envios e **k** o número de e-mails distintos, a consulta de pertinência na lista pode percorrer os inscritos já acumulados. O custo é **O(nk)**, chegando a **O(n²)** com todos distintos, no modelo que trata comparações de strings como custo constante. Se o tamanho dos e-mails entrar na análise, o custo das comparações também deve ser considerado.

O resultado ocupa **O(k)** e o espaço auxiliar fora dele é **O(1)**. Não há requisito de desempenho que torne essa escolha incorreta. Uma estrutura alternativa de consulta pode ser discutida depois que o aluno explicar a abordagem; não há exigência de otimizar agora.

### Aprendizagem e apoio recebido

| Competência | Classificação | Evidência e limite |
| --- | --- | --- |
| Eliminar repetições preservando ordem | Progresso parcial | Implementação correta no 002; explicação do aluno ainda não apresentada. |
| Construir asserts e comparar retorno completo | Progresso parcial | Aplicação na primeira tentativa após orientação no 001; cenários ainda se restringem ao exemplo e vazio. |
| Verificar preservação da entrada | Progresso parcial | Uso correto reaplicado; independência da saída ainda não testada pelo aluno. |
| Analisar custo de busca em lista | Ainda não avaliado | A análise acima é do assistente. |

O enunciado e a orientação anterior sobre testes foram fornecidos pelo assistente. Não foi fornecida solução do 002 no contexto acessível. Não se atribui ao aluno raciocínio ou justificativa ainda não apresentado.

### Retomada

Pergunta: **por que adicionar um e-mail somente quando ele ainda não está em inscritos preserva a ordem da primeira ocorrência?**

Depois, trabalhar os testes de ordem não alfabética e independência da saída. Não é necessário reescrever a função ou introduzir framework. Nenhum código ou teste do aluno foi alterado.
