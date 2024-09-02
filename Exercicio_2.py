#Tarefa_02

def menor_diferenca(nums):
    # Ordena o array
    nums.sort()
    # Inicializa a menor diferença com um valor maior
    menor_dif = float('inf')
    # Inicializa o par com None
    par = None
    
    # Percorrerar o array e comparara as diferenças entre os elementos adjacentes
    for i in range(len(nums) - 1):
        dif = nums[i + 1] - nums[i]
        if dif < menor_dif:
            menor_dif = dif
            par = (nums[i], nums[i + 1])
    
    return par
