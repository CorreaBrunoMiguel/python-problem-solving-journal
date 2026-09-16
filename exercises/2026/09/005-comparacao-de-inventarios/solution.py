# Código-base fornecido pelo assistente de IA; implementação a cargo do aluno.


def comparar_inventarios(anterior, atual):
    """
    Compara nomes e tamanhos de arquivos entre dois inventários.

    Args:
        anterior: Dicionário de nomes de arquivos para tamanhos em bytes
            antes da atualização. Tamanhos são inteiros não negativos.
        atual: Dicionário no mesmo formato, após a atualização.

    Returns:
        Dicionário com três listas de nomes em ordem alfabética:
            - adicionados: nomes presentes apenas no inventário atual.
            - removidos: nomes presentes apenas no inventário anterior.
            - alterados: nomes presentes nos dois, com tamanhos diferentes.

        Categorias sem ocorrências são representadas por listas vazias.

    Notes:
        Zero é um tamanho válido e não indica ausência do arquivo.
        Mesmo nome e tamanho são considerados sem alteração.
        As entradas não são modificadas e as listas retornadas são
        independentes. Não há acesso ao sistema de arquivos.
    """
    pass
