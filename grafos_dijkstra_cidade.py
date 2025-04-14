"""
Algoritmo de Dijkstra: Cidade apenas com semáforos. 
Busca a partir do vértice de origem para um vértice de destino. 
"""


import heapq

def dijkstra(grafo, tempos, origem, destino):
    distancias = {vertice: float('inf') for vertice in grafo}
    caminho = {vertice: None for vertice in grafo}
    distancias[origem] = 0
    heap = [(0, origem)]
    
    while heap:
        tempo_atual, vertice_atual = heapq.heappop(heap)

        if vertice_atual == destino:
            trajeto = []
            while vertice_atual:
                trajeto.append(vertice_atual)
                vertice_atual = caminho[vertice_atual]
            return tempo_atual, trajeto[::-1]
        
        for vizinho, (distancia, v_max) in grafo[vertice_atual].items():
            tempo_viagem = distancia / v_max
            novo_tempo = tempo_atual + tempo_viagem
            
            while novo_tempo in tempos[vizinho]:
                novo_tempo += 1
            
            if novo_tempo < distancias[vizinho]:
                distancias[vizinho] = novo_tempo
                caminho[vizinho] = vertice_atual
                heapq.heappush(heap, (novo_tempo, vizinho))
    
    return -1, []

grafo = {}
tempos = {}
n, m = input().split()

for i in range(1, int(n) + 1):
    grafo[str(i)] = {}
    tempos[str(i)] = []

for _ in range(int(m)):
    u, v, w, v_max = input().split()
    grafo[u][v] = (int(w), int(v_max))

for i in range(1, int(n) + 1):
    entrada = input().split()

    if entrada[0] != "0":
        tempos[str(i)] = [int(x) for x in entrada[1:]]

tempo, caminho = dijkstra(grafo, tempos, "1", n)
print(f"Tempo total: tempo. Caminho: {' -> '.join(caminho)}")