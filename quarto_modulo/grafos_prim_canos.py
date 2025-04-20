"""
Algoritmo de Prim: Algoritmo para conectar todos os canos com o menor custo.
"""

import heapq, math

grafo = {}
m, n = input().split()

for i in range(1, int(m) + 1):
    grafo[str(i)] = {}

for _ in range(int(n)):
    a, b, c = input().split()
    grafo[a][b] = int(c)


def grafos_prim_aula(grafo, vertice_origem: str):
    key = {v: math.inf for v in grafo}
    pai = {v: None for v in grafo}
    key[vertice_origem] = 0
    
    fila = [(0, vertice_origem)]
    visitados = set()
    
    soma = 0
    conectados = 0
    
    while fila:
        peso_u, u = heapq.heappop(fila)

        if u in visitados:
            continue
        visitados.add(u)
        
        soma += peso_u
        conectados += 1
        
        for v, peso_uv in grafo[u].items():
            if v not in visitados and peso_uv < key[v]:
                key[v] = peso_uv
                pai[v] = u
                heapq.heappush(fila, (key[v], v))
    
    return conectados, soma


menor_distancia = float('inf')
tamanho_grafo = len(grafo)

for v in grafo:
    quantidade_v_conectados, menor_distancia_i = grafos_prim_aula(grafo=grafo, vertice_origem=v)
    if quantidade_v_conectados == tamanho_grafo:
        if menor_distancia_i < menor_distancia:
            menor_distancia = menor_distancia_i

print(menor_distancia)