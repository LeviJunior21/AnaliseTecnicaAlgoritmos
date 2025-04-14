"""
Vou ao cassino diariamente. Todo dia ganho uma certa quantia. Infelizmente a quantia é muitas vezes negativa. 
Meus amigos querem saber qual foi a sequência de dias, na minha história de idas ao cassino, em que meu ganho acumulado foi máximo. 
A tabela abaixo dá um exemplo para um período de 8 dias. 
Nesse exemplo, o ganho acumulado foi máximo ($35) no período que vai do dia 3 ao dia 6.
"""

class MaxSumSegment:
    def __init__(self, array=list[int]):
        self.array = array
        self.resultado = self.max_sum_segment(inicio=0, fim=(len(array) - 1))
        
    def max_sum_segment(self, inicio: int, fim: int) -> int:
        if (inicio == fim):
            return self.array[inicio]
        
        meio = (inicio + fim) // 2
        x1 = self.max_sum_segment(inicio=inicio, fim=meio)
        x2 = self.max_sum_segment(inicio=meio+1, fim=fim)
        
        y1 = s = self.array[meio]
        for i in range(meio - 1, inicio, -1):
            s += self.array[i]
            y1 = max(y1, s)
        
        y2 = s = self.array[meio + 1]
        for i in range(meio + 2, fim):
            s += self.array[i]
            y2 = max(y2, s)
        
        return max(x1, y1+y2, x2)

array = [20, -30, 15, -10, 30, -20, -30, 30]
max_sum_segment = MaxSumSegment(array=array)
print(max_sum_segment.resultado)