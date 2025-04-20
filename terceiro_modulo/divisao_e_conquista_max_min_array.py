"""
Problema: Encontre os elementos máximo e mínimo em uma matriz S[1..n]. Quantas comparações entre elementos de S são necessárias?
"""

class MaxMinArray:
    def __init__(self, array: list[int]):
        self.array = array
        self.result = self.max_min(inicio=0, fim=(len(array) - 1))
    
    def max_min(self, inicio: int, fim: int):
        if (inicio == fim): return self.array[inicio], self.array[inicio]
        
        meio = (inicio + fim) // 2
        max_left, min_left = self.max_min(inicio=inicio, fim=meio)
        max_right, min_right = self.max_min(inicio=meio+1, fim=fim)
        
        if (max_left >= max_right):
            maximo = max_left
        else:
            maximo = max_right
        
        if (min_left <= min_right):
            minimo = min_left
        else:
            minimo = min_right
        
        return (maximo, minimo)
    
array = [20, -30, 15, -10, 100, 30, -20, -30, 30, -200]
max_min_array = MaxMinArray(array=array)
print(max_min_array.result)