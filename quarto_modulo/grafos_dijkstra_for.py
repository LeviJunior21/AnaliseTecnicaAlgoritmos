"""
Algorimo de Dijkstra: Algoritmo com laço For
Custo total: O(V² + E)
"""

import math

vertices = {
    "s": {"d": 9,  "a": 15},
    "a": {"b": 35, "c": 3},
    "b": {"a": 16, "c": 6, "t": 21},
    "c": {"d": 2,  "t": 7},
    "d": {"a": 4,  "c": 2},
    "t": {"b": 5}
}

tabela = {}
usados = []
for vertice in vertices.keys():
    tabela[vertice] = [math.inf, None]
    usados.append(vertice)

def dijkstra(origem, usados, tabela):
    for vizinho in vertices[origem]:
        nova_distancia = tabela[origem][0] + vertices[origem][vizinho]
        if nova_distancia < tabela[vizinho][0]:
            tabela[vizinho] = [nova_distancia, origem]
    
    usados.remove(origem)
    if not usados: return
    
    menor = None
    menor_distancia = math.inf
    for vertice in usados:
        if tabela[vertice][0] < menor_distancia:
            menor_distancia = tabela[vertice][0]
            menor = vertice
    
    if menor is not None:
        dijkstra(origem=menor, usados=usados, tabela=tabela)

def run(origem, usados, tabela):
    tabela[origem][0] = 0
    dijkstra(origem=origem, usados=usados, tabela=tabela)

    for vertice in tabela:
        print(f"{vertice}: distância = {tabela[vertice][0]}, anterior = {tabela[vertice][1]}")

vertice_origem = "s"
run(vertice_origem, usados=usados, tabela=tabela)