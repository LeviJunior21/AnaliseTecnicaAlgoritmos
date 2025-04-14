"""
Dado um array A de números distintos, encontrar a quantidade de pares de elementos (A[i],A[j]), tal que i < j e A[i] > A[j].
"""

import math

class MergeSort:
    def __init__(self, array: list[int]):
        self.array = array
        self.count = self.mergeSort(inicio=0, fim=len(array))
    
    def mergeSort(self, inicio: int, fim: int) -> None:
        if (fim - inicio == 1): return 0
        meio = (inicio + fim) // 2
        x = self.mergeSort(inicio=inicio, fim=meio)
        y = self.mergeSort(inicio=meio, fim=fim)
        z = self.merge(inicio=inicio, meio=meio, fim=fim)
        return x + y + z
    
    def merge(self, inicio: int, meio: int, fim: int) -> None:
        array1Aux: list[int] = self.array[inicio : meio] + [math.inf]
        array2Aux: list[int] = self.array[meio: fim] + [math.inf]
        count = aux1_i = aux2_i = 0
        
        for i in range(inicio, fim):
            if (array1Aux[aux1_i] <= array2Aux[aux2_i]):
                self.array[i] = array1Aux[aux1_i]
                aux1_i += 1
            else:
                self.array[i] = array2Aux[aux2_i]
                aux2_i += 1
                count += len(array1Aux) - aux1_i
        
        return count

array1 = [9,8,7,6,5,4,3,2,1]
array2 = [8,3,2,9,7,1,5,4]
array3 = [8,3,3]
array4 = [9]
array5 = [1,2,3,4,5,6,7,8,9]
array6 = [1,2,3,4,5,6,7,9,8]

array = array2

mergeSort = MergeSort(array=array)
print(array)
print(mergeSort.count)