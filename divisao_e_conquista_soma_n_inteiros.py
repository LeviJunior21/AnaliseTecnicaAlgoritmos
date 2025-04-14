"""
Somar todos os elementos do array.
"""

class SomaInteiros:
    def __init__(self, array: list[int]):
        self.array = array
        self.resultado = self.somar(inicio=0, fim=(len(array) - 1))
        
    def somar(self, inicio: int, fim: int) -> int:
        if (inicio == fim):
            return self.array[inicio]
        
        meio = (inicio + fim) // 2
        x1 = self.somar(inicio=inicio, fim=meio)
        x2 = self.somar(inicio=meio+1, fim=fim)
        
        return x1 + x2

array = [1,2,3,4,5,6,7,8,9,10]
soma_inteiros = SomaInteiros(array=array)
print(soma_inteiros.resultado)