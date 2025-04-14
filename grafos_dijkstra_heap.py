"""
Algoritmo de Dijkstra: Algoritmo básico com heap.
"""

import heapq

def dijkstra(grafo, origem):
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[origem] = 0
    
    heap = [(0, origem)]
    
    while heap:
        distancia_atual, vertice_atual = heapq.heappop(heap)
        
        for vizinho, peso in grafo[vertice_atual].items():
            nova_distancia = distancia_atual + peso
            
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                heapq.heappush(heap, (nova_distancia, vizinho))
    
    return distancias

vertices = {
    "s": {"d": 9,  "a": 15},
    "a": {"b": 35, "c": 3},
    "b": {"a": 16, "c": 6, "t": 21},
    "c": {"d": 2,  "t": 7},
    "d": {"a": 4,  "c": 2},
    "t": {"b": 5}
}

print(dijkstra(vertices, "s"))