"""
Algoritmo de Dijkstra: Algoritmo básico com vértice de origem e destino.
"""

import heapq

def dijkstra(grafo, tempos, origem, destino):
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[origem] = 0
    heap = [(0, origem)]
    
    while heap:
        distancia_atual, vertice_atual = heapq.heappop(heap)

        if distancia_atual > distancias[vertice_atual]:
            continue

        if vertice_atual == destino:
            return distancia_atual
        
        for vizinho, peso in grafo[vertice_atual].items():
            nova_distancia = distancia_atual + peso
            
            while nova_distancia in tempos[vizinho]:
                nova_distancia += 1
            
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                heapq.heappush(heap, (nova_distancia, vizinho))
    
    return -1


grafo = {}
tempos = {}
n, m = input().split()

for i in range(1, int(n) + 1):
    grafo[str(i)] = {}
    tempos[str(i)] = []

for _ in range(int(m)):
    u, v, w = input().split()
    grafo[u][v] = int(w)

for i in range(1, int(n) + 1):
    entrada = input().split()

    if entrada[0] != "0":
        tempos[str(i)] = [int(x) for x in entrada[1:]]

print(dijkstra(grafo, tempos, "1", n))
