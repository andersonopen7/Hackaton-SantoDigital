#Tarefa_03

def subconjuntos(nums):
    resultado = [[]]
    for num in nums:
        resultado += [item + [num] for item in resultado]
    return resultado

#Como exemplo e forma de uso, Com base na entrada, se entrada = [1, 2]
#saida = subconjuntos(entrada) print(saida)

