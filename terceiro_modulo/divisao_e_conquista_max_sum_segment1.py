"""
Vou ao cassino diariamente. Todo dia ganho uma certa quantia. Infelizmente a quantia é muitas vezes negativa. 
Meus amigos querem saber qual foi a sequência de dias, na minha história de idas ao cassino, em que meu ganho acumulado foi máximo. 
A tabela abaixo dá um exemplo para um período de 8 dias. 
Nesse exemplo, o ganho acumulado foi máximo ($35) no período que vai do dia 3 ao dia 6.
"""

class MaxSumSegment:
    def __init__(self, array: list[int]):
        self.array = array
        self.resultado = self.max_sum_segment(len(array) - 1)
        
    def max_sum_segment(self, tamanho) -> int:
        solucao = self.array[0]
        for i in range(tamanho):
            for j in range(i, tamanho):
                x = 0
                for n in range(i, j):
                    x += self.array[n]
                solucao = max(solucao, x)
        return solucao
    
array = [20, -30, 15, -10, 30, -20, -30, 30]
max_sum_segment = MaxSumSegment(array=array)
print(max_sum_segment.resultado)