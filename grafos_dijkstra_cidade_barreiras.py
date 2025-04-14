"""
Algoritmo de Dijkstra: Cidade com barreiras no formato de matrizes. 
"""

labirinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1]
]

pontos = {
    'A': (0, 0),
    'B': (0, 2),
    'C': (0, 4),
    'D': (5, 2)
}

import heapq

def dijkstra_labirinto_com_caminho(labirinto, origem, destino):
    linhas, colunas = len(labirinto), len(labirinto[0])
    distancias = [[float('inf')] * colunas for _ in range(linhas)]
    distancias[origem[0]][origem[1]] = 0
    
    caminho = {}
    heap = [(0, origem)]
    
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    nomes_direcoes = {
        (-1, 0): 'cima',
        (1, 0): 'baixo',
        (0, -1): 'esquerda',
        (0, 1): 'direita'
    }
    
    while heap:
        distancia_atual, (linha, coluna) = heapq.heappop(heap)
        
        for dl, dc in direcoes:
            nova_linha, nova_coluna = linha + dl, coluna + dc
            
            if 0 <= nova_linha < linhas and 0 <= nova_coluna < colunas:
                if labirinto[nova_linha][nova_coluna] == 0:
                    nova_distancia = distancia_atual + 1
                    
                    if nova_distancia < distancias[nova_linha][nova_coluna]:
                        distancias[nova_linha][nova_coluna] = nova_distancia
                        heapq.heappush(heap, (nova_distancia, (nova_linha, nova_coluna)))
                        caminho[(nova_linha, nova_coluna)] = (linha, coluna)
    
    passos = []
    atual = destino
    while atual != origem:
        anterior = caminho.get(atual)
        if anterior is None:
            return None
        dl = atual[0] - anterior[0]
        dc = atual[1] - anterior[1]
        passos.append(nomes_direcoes[(dl, dc)])
        atual = anterior
    
    passos.reverse()
    return passos

rotas = {}
origem = pontos["A"]

for destino_nome in ["B", "C", "D"]:
    destino = pontos[destino_nome]
    passos = dijkstra_labirinto_com_caminho(labirinto, origem, destino)
    if passos:
        rotas[destino_nome] = passos
    else:
        rotas[destino_nome] = "Sem caminho possível"

for destino, caminho in rotas.items():
    print(f"A → {destino}:")
    print(f"  Caminho: {caminho}")
    print(f"  Passos: {len(caminho) if isinstance(caminho, list) else '∞'}")
    print()
