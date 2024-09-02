

#Tarefa_01

def lista_asteriscos(n):
    return ['*' * i for i in range(1, n + 1)]
 lista_de_asteriscos.append('*'*i) #A cada iteração adiciono à lista_de_asteriscos uma string contendo o numero de asteriscos igual ao valor de i na interação, que começa com 1 e vai até o numero digitado pelo usuário
    return lista_de_asteriscos

numero = int(input("Digite um numero inteiro: ")) 

lista_de_asteriscos = lista_asteriscos(numero) #Chama a função 'gerar_lista_asteriscos' e guarda o valor retornado por ela na variável 'lista_de_asteriscos'

print(lista_de_asteriscos) 


------------------------------------------------------------------------------------------------

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


---------------------------------------------------------------------------------------------------

#Tarefa_03

def subconjuntos(nums):
    resultado = [[]]
    for num in nums:
        resultado += [item + [num] for item in resultado]
    return resultado

#Como exemplo e forma de uso, Com base na entrada, se entrada = [1, 2]
#saida = subconjuntos(entrada) print(saida)




