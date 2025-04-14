"""
Algortimo de Bellman-Ford: Algoritmo para identificar ciclos em um grafo.
"""

import math

grafo = {
    "z": {"u": 6, "x": 7},
    "u": {"x": 8, "v": 5, "y": -4},
    "v": {"u": -2},
    "x": {"v": -3, "y": 9},
    "y": {"z": 2, "v": 7}
}
origem = "z"

grafo = {
    "a": {"b": 2, "d": 10},
    "b": {"d": 3},
    "d": {"c": 12},
    "c": {"b": -25}
}
origem = "a"

def bellman_ford(grafo, origem):
    combinacoes = []
    for u in grafo:
        for v in grafo[u]:
            combinacoes.append((u, v))
            
    dist = {}
    for vertice in grafo:
        dist[vertice] = math.inf
    
    dist[origem] = 0
    
    for _ in range(len(grafo) - 1):
        for u, v in combinacoes:
            soma = dist[u] + grafo[u][v]
            if soma < dist[v]:
                dist[v] = soma
        
    for u, v in combinacoes:
        soma = dist[u] + grafo[u][v]
        if soma < dist[v]:
            return False
    
    return True

resultado = bellman_ford(grafo=grafo, origem=origem)
print(resultado)