"""
Ordenar array usando o MergeSort com laço while.
"""

class MergeSort:
    def __init__(self, array: list[int]):
        self.array = array
        self.mergeSort(inicio=0, fim=len(array) - 1)
        
    def mergeSort(self, inicio: int, fim: int):
        if (inicio < fim):
            meio = (inicio + fim) // 2
            self.mergeSort(inicio=inicio, fim=meio)
            self.mergeSort(inicio=meio + 1, fim=fim)
            self.merge(inicio=inicio, meio=meio, fim=fim)
                    
    def merge(self, inicio: int, meio: int, fim: int):
        array1Aux = [self.array[i] for i in range(inicio, meio + 1)]
        array2Aux = [self.array[i] for i in range(meio + 1,fim + 1)]
        
        i = inicio
        aux1_i = 0
        aux2_i = 0
        
        while (aux1_i < len(array1Aux) and aux2_i < len(array2Aux)):
            if (array1Aux[aux1_i] <= array2Aux[aux2_i]):
                self.array[i] = array1Aux[aux1_i]
                aux1_i += 1
            else:
                self.array[i] = array2Aux[aux2_i]
                aux2_i += 1
            i += 1
        
        while (aux1_i < len(array1Aux)):
            self.array[i] = array1Aux[aux1_i]
            aux1_i += 1
            i += 1
            
        while (aux2_i < len(array2Aux)):
            self.array[i] = array2Aux[aux2_i]
            aux2_i += 1
            i += 1

array = [9,8,7,6,5,4,3,2,1]
mergeSort = MergeSort(array=array)

print(array)