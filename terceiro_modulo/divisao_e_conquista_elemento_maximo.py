"""
Encontre o maior elemento do array.
"""

class ElementoMaximo:
    def __init__(self, array: list[int]):
        self.array = array
        self.resultado = self.maximo(inicio=0, fim=(len(array) - 1))
        
    def maximo(self, inicio: int, fim: int) -> int:
        if (inicio == fim):
            return self.array[inicio]
        
        meio = (inicio + fim) // 2
        x1 = self.maximo(inicio=inicio, fim=meio)
        x2 = self.maximo(inicio=meio+1, fim=fim)
        
        if (x1 >= x2): return x1
        return x2

array = [1,2,3,4,5,6,7,8,9,10]
soma_inteiros = ElementoMaximo(array=array)
print(soma_inteiros.resultado)