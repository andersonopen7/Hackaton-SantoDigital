from itertools import chain, combinations

def all_subsets(nums, max_size=None, min_size=None, distinct_only=False, sort_subsets=False):
    # Função para gerar todos os subconjuntos
    def subsets(nums):
        return chain(*map(lambda x: combinations(nums, x), range(len(nums) + 1)))

    # Removera duplicatas se distinct_only for True
    if distinct_only:
        nums = list(set(nums))

    # Gera todos os subconjuntos
    all_subsets = list(subsets(nums))

    # Filtrarar por tamanho mínimo e máximo
    if min_size is not None:
        all_subsets = [s for s in all_subsets if len(s) >= min_size]
    if max_size is not None:
        all_subsets = [s for s in all_subsets if len(s) <= max_size]

    # Ordenar subconjuntos e elementos dentro dos subconjuntos se sort_subsets for True
    if sort_subsets:
        all_subsets = [tuple(sorted(s)) for s in all_subsets]
        all_subsets.sort()

    return all_subsets
