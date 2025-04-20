"""
Encontrar um dado CPF numa longa lista de números de CPF.
"""

class BinarySearch:
    def __init__(self, array: list[int], valor: int):
        self.array: list[int] = array
        self.valor: int = valor
        self.result = self.binary_search(inicio=0, fim=len(array) - 1)
        
    def binary_search(self, inicio: int, fim: int):
        if inicio == fim: return -1
        
        meio = (inicio + fim) // 2
        
        if (self.array[meio] == self.valor): return meio
        elif (self.valor > self.array[meio]):
            return self.binary_search(inicio=meio+1, fim=fim)
        return self.binary_search(inicio=inicio, fim=meio-1)

array = [1,5,6,10,14,20,40,100]
valor = 1000
binary_search = BinarySearch(array=array, valor=valor)
print(binary_search.result)