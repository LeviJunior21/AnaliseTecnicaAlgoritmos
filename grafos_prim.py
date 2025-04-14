"""
Algoritmo de Prim: Algoritmo visto em aula.
"""

import heapq

grafo = {
    "0": {"1": 6, "2": 1, "3": 5},
    "1": {"0": 6, "2": 2, "4": 5},
    "2": {"0": 1, "1": 2, "3": 2, "4": 6, "5": 4},
    "3": {"0": 5, "2": 2, "5": 4},
    "4": {"1": 5, "2": 6, "5": 3},
    "5": {"2": 4, "3": 4, "4": 3}
}

def prim_dfs(grafo, vertice_origem):
    heap = [(peso, vertice_origem, destino) for destino, peso in grafo[vertice_origem].items()]
    heapq.heapify(heap)
    usados = {vertice_origem}
    lista = []
    
    while heap:
        peso, origem, destino = heapq.heappop(heap)
        
        if destino not in usados:
            usados.add(destino)
            lista.append((peso, origem, destino))
            
            for vizinho, peso_vizinho in grafo[destino].items():
                if vizinho not in usados:
                    heapq.heappush(heap, (peso_vizinho, destino, vizinho)) 

    return lista

lista = prim_dfs(grafo=grafo, vertice_origem="0")
print(lista)