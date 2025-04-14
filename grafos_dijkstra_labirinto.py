"""
Algoritmo de Dijkstra: Algoritmo do labirinto. 
"""

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

labirinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0]
]

origem = (0, 0)
destino = (3, 4)

passos = dijkstra_labirinto_com_caminho(labirinto, origem, destino)

if passos:
    print("Passos até o destino:", " → ".join(passos))
else:
    print("Não há caminho possível até o destino.")
