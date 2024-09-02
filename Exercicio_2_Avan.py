def pares_menor_diferenca(arr, allow_duplicates=True, sorted_pairs=False, unique_pairs=False):
    if not arr or len(arr) < 2:
        return []

    arr.sort()
    min_diff = float('inf')
    pares = []

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if not allow_duplicates and arr[i] == arr[j]:
                continue
            diff = abs(arr[i] - arr[j])
            if diff < min_diff:
                min_diff = diff
                pares = [(arr[i], arr[j])]
            elif diff == min_diff:
                pares.append((arr[i], arr[j]))

    if unique_pairs:
        pares = list(set(tuple(sorted(par)) for par in pares))

    if sorted_pairs:
        pares = [tuple(sorted(par)) for par in pares]
        pares.sort()

    return pares

# Exemplo de uso
arr = [4, 2, 1, 3, 5]
resultado = pares_menor_diferenca(arr, allow_duplicates=False, sorted_pairs=True, unique_pairs=True)
print(resultado)


#Explicação:
Ordenação do array: A função começa ordenando o array para facilitar a comparação dos pares.
Cálculo da menor diferença: A função percorre todos os pares possíveis e calcula a diferença absoluta entre eles, mantendo o controle do menor valor encontrado.
Parâmetros opcionais:
allow_duplicates: Se False, a função ignora pares com valores duplicados.
sorted_pairs: Se True, os pares no resultado são ordenados em ordem crescente.
unique_pairs: Se True, a função retorna apenas pares únicos, considerando (a, b) e (b, a) como o mesmo par.
No exemplo fornecido, a função retorna os pares com a menor diferença absoluta, respeitando as configurações dos parâmetros opcionais.
