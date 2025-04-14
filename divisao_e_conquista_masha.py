class Masha:
    def __init__(self, array: list[int], tamanho: int):
        self.array = array
        self.tamanho = tamanho
        self.conta = 0
        self.array_ordenado = self.masha(inicio=0, fim=tamanho-1)
    
    def masha(self, inicio: int, fim: int) -> list[int]:
        if inicio == fim: return [self.array[inicio]]
        meio = (inicio + fim) // 2
        esquerda = self.masha(inicio=inicio, fim=meio)
        direita = self.masha(inicio=meio+1, fim=fim)
        
        if esquerda[-1] > direita[0]:
            self.conta += 1
            return direita + esquerda
        
        return esquerda + direita
    
    def processa(self) -> int:
        ordenado =  all(self.array_ordenado[i] <= self.array_ordenado[i+1] for i in range(len(self.array_ordenado) - 1))
        return self.conta if ordenado else -1


entradas = int(input())
armazenamento = []

for _ in range(entradas):
    tamanho_entrada = int(input())
    valores_entrada = [int(x) for x in input().split()]
    armazenamento.append([valores_entrada, tamanho_entrada])

for valores_entrada, tamanho_entrada in armazenamento:
    masha = Masha(array=valores_entrada, tamanho=tamanho_entrada)
    print(masha.processa())
