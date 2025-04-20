class ArrayBitonic:
    def __init__(self, array: list[int]):
        self.array = array
        self.last_index = len(array) - 1
        self.resultado = self.array_bitonic(inicio=0, fim=self.last_index)
    
    def array_bitonic(self, inicio: int, fim: int) -> int:
        if inicio == fim: return inicio
        
        meio = (inicio + fim) // 2
        if (0 < meio < self.last_index):
            if (self.array[meio - 1] < self.array[meio] > self.array[meio + 1]): return meio
        
        if (meio < self.last_index and self.array[meio + 1] > self.array[meio]):
            return self.array_bitonic(inicio=meio+1, fim=fim)
        else:
            return self.array_bitonic(inicio=inicio, fim=meio)
        

array = [1,2,3,4,5,6,7,8,9,10]
array = [10,9,8,7,6,5,4,3,2,1]
array = [1,2,3,4,5,6,7,8,9,10,5,4,3,2,1]
array_bitonic = ArrayBitonic(array=array)
print(array_bitonic.resultado)