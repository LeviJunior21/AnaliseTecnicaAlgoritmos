"""
Ordenar array usando o MergeSort com laço for.
"""

import math

class MergeSort:
    def __init__(self, array: list[int]):
        self.array = array
        self.mergeSort(inicio=0, fim=len(array))
    
    def mergeSort(self, inicio: int, fim: int) -> None:
        if (inicio >= fim - 1): return
        meio = (inicio + fim) // 2
        self.mergeSort(inicio=inicio, fim=meio)
        self.mergeSort(inicio=meio, fim=fim)
        self.merge(inicio=inicio, meio=meio, fim=fim)
    
    def merge(self, inicio: int, meio: int, fim: int) -> None:
        esquerda: list[int] = self.array[inicio : meio] + [math.inf]
        direita: list[int] = self.array[meio: fim] + [math.inf]
        aux1_i = aux2_i = 0
        
        for i in range(inicio, fim):
            if (esquerda[aux1_i] <= direita[aux2_i]):
                self.array[i] = esquerda[aux1_i]
                aux1_i += 1
            else:
                self.array[i] = direita[aux2_i]
                aux2_i += 1

array = [9,8,7,6,5,4,3,2,1]
mergeSort = MergeSort(array=array)
print(array)