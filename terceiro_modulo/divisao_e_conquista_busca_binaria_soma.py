"""
É dado um número inteiro s e um vetor crescente A[1..n] de números inteiros. 
Quero saber se existem dois elementos do vetor cuja soma é exatamente s. 
Dê um algoritmo que resolva o problema em tempo O(nlg(n)).
"""

class BuscaBinariaSoma:
    def __init__(self, array: list[int], soma: int):
        self.array = array
        self.s = soma
        self.result = self.soma(soma=soma, inicio=0, fim=(len(array) - 1))
    
    def soma(self, soma: int, inicio: int, fim: int) -> bool:
        for i in range(fim):
            if self.busca_binaria(inicio=inicio, fim=i, resto=(soma-self.array[i])):
                return True
            if self.busca_binaria(inicio=i+1, fim=fim, resto=(soma-self.array[i])):
                return True

        return False
        
    def busca_binaria(self, inicio: int, fim: int, resto) -> bool:
        if (inicio > fim): return False
        
        meio = (inicio + fim) // 2
        if self.array[meio] == resto:
            return True
        
        if (resto > self.array[meio]):
            return self.busca_binaria(inicio=meio+1, fim=fim, resto=resto)
        return self.busca_binaria(inicio=inicio, fim=meio)

array = [1,2,3,4,5,6]
soma = 10
busca_binaria_soma = BuscaBinariaSoma(array=array, soma=soma)
print(busca_binaria_soma.result)
