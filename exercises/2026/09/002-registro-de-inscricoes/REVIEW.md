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

## Revisão 02 — 11/09/2026 — Encerramento

- **Commit:** [be148f4](https://github.com/CorreaBrunoMiguel/python-problem-solving-journal/commit/be148f44f4a8da83e55750fd334f3eca7cff1e82).
- **Mensagem:** `test: verifica ordem de chegada e independência da saída no desafio 002`.
- **Estado:** concluído no escopo do desafio, com orientação na ampliação dos testes.
- **Mudança analisada:** somente `test_solution.py`; a função permanece inalterada.

### Verificação executada

Executado o arquivo de testes com a solução do commit em Python 3.12.14 no ambiente do assistente. **Os 13 asserts passaram**, com saída vazia e código de saída zero. São três cenários: e-mails repetidos, lista vazia e e-mails únicos.

Não foi repetida a bateria adicional da primeira revisão: a função não mudou e o risco concreto desta entrega estava nos novos testes.

### Pendências resolvidas

- **Ordem de chegada:** a lista com repetições agora começa por Carla, Ana, Eduardo, Bruno e Fernanda nas primeiras ocorrências. O retorno esperado respeita essa ordem não alfabética, e o total foi corretamente atualizado para quatro repetições.
- **Entrada sem repetições:** foi acrescentado um cenário com seis e-mails únicos em ordem não alfabética, com comparação da lista e do retorno completo, e contagem zero.
- **Independência da saída:** o aluno copia a entrada antes da chamada, obtém o resultado, acrescenta Leo à lista retornada e compara a entrada com a cópia original. O teste passou e verificaria o compartilhamento indevido da lista nesse cenário. A saída não foi copiada artificialmente antes do append.
- **Preservação da entrada:** a verificação anterior do caso com repetições permanece presente e passou.

### Compreensão e apoio recebido

O aluno explicou que percorre os elementos na ordem de chegada, adiciona apenas os ainda ausentes e usa append, que acrescenta ao final. Essa explicação sustenta o entendimento da preservação das primeiras ocorrências. O assistente apenas ajustou a referência aos índices: for percorre elementos; o último índice positivo é n - 1, e -1 é uma indexação alternativa do último elemento.

Houve orientação detalhada para o teste de independência: distinção entre preservação durante a chamada e alteração posterior da saída, uso de entrada sem repetições, cópia da entrada e não do retorno. O aluno implementou o teste, mas sua construção não é evidência de resolução inteiramente autônoma.

A capacidade de construir verificações apresenta progresso; independência de objetos deve ser retomada futuramente para observar retenção. Complexidade continua sem explicação do aluno e, portanto, ainda não avaliada como competência dele. Nenhuma implementação completa foi fornecida pelo assistente no contexto disponível.

### Melhorias não bloqueantes

Continuam registradas a ambiguidade da docstring sobre repetidas, a expressão “entrada nula”, a ordem dos imports, detalhes de espaços e alinhamento e a quebra de linha final da solução. São melhorias de apresentação e precisão; não comprometem o comportamento e não motivam outra rodada obrigatória de commits.

Os asserts sobre campos, extremos e objeto completo têm alguma redundância, aceitável nesta etapa. Não é necessário removê-los ou otimizar o algoritmo para concluir.

### Encerramento

Requisitos essenciais atendidos, verificações combinadas realizadas e explicação central apresentada. O desafio está concluído, sem equivaler a domínio consolidado. Nenhum código ou teste do aluno foi alterado pelo assistente; a primeira análise permanece preservada.
