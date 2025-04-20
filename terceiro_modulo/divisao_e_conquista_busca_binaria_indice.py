"""
Um vetor A[1..n] de números inteiros é semi-compacto se A[i+1]-A[i] ≤ 1 para i = 1,2,…,n-1. 
Escreva um algoritmo que receba um vetor semi-compacto A[1..n] e um inteiro x tais que A[1] ≤ x ≤ A[n] e 
devolva um índice i no intervalo 1..n tal que A[i] = x. Seu algoritmo deve consumir O(lg(n)) unidades de tempo.
"""

class BuscaBinariaIndice:
    def __init__(self, array: list[int], x:int):
        self.array = array
        self.x = x
        self.resultado = self.busca_binaria_indice(inicio=0, fim=len(array) - 1)
    
    def busca_binaria_indice(self, inicio: int, fim: int) -> int:
        if (inicio == fim and self.x == self.array[fim]): return fim
        elif (inicio == fim): return None
        
        meio = (inicio + fim) // 2
        
        if (self.array[meio] == self.x):
            if (meio + 1 <= fim and self.array[meio + 1] == self.x):
                return self.busca_binaria_indice(inicio=meio+1, fim=fim)

            return meio
        
        if (self.x > self.array[meio]):
            return self.busca_binaria_indice(inicio=meio+1, fim=fim)
        return self.busca_binaria_indice(inicio=inicio, fim=meio)

array = [1,1,1,1,1,1,1,1,1,2,2,3,3,4]
x = 3
busca_binaria_indice = BuscaBinariaIndice(array=array, x=x)
indice = busca_binaria_indice.resultado
print(indice)