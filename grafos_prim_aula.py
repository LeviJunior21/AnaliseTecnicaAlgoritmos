"""
Algoritmo de Prim: Algoritmo para conectar todos os vértices com o menor custo.
"""

import math, heapq

grafo = {
    "0": {"1": 6, "2": 1, "3": 5},
    "1": {"0": 6, "2": 2, "4": 5},
    "2": {"0": 1, "1": 2, "3": 2, "4": 6, "5": 4},
    "3": {"0": 5, "2": 2, "5": 4},
    "4": {"1": 5, "2": 6, "5": 3},
    "5": {"2": 4, "3": 4, "4": 3}
}

origem = "0"

grafo = {
    "a": {"b": 4, "h": 8},
    "b": {"c": 8, "a": 4, "h": 11},
    "c": {"b": 8, "d": 7, "i": 2, "f": 4},
    "d": {"c": 7, "f": 14, "e": 9},
    "e": {"d": 9, "f": 10},
    "f": {"c": 4, "d": 14, "e": 10, "g": 2},
    "g": {"i": 6, "f": 2, "h": 1},
    "h": {"g": 1, "i": 7, "b": 11, "a": 8},
    "i": {"c": 2, "h": 7, "g": 6}
}

origem = "a"

def grafos_prim_aula(grafo, vertice_origem: str):
    key = {v: math.inf for v in grafo}
    pai = {v: None for v in grafo}
    key[vertice_origem] = 0
    
    fila = [(0, vertice_origem)]
    visitados = set()
    
    while fila:
        peso_u, u = heapq.heappop(fila)
        
        if u in visitados:
            continue
        visitados.add(u)
        
        for v, peso_uv in grafo[u].items():
            if v not in visitados and peso_uv < key[v]:
                key[v] = peso_uv
                pai[v] = u
                heapq.heappush(fila, (key[v], v))
    
    mst = []
    for v in grafo:
        if pai[v] is not None:
            mst.append((pai[v], v, grafo[pai[v]][v]))
    
    return mst

print(grafos_prim_aula(grafo, origem))