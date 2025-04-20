"""
Algoritmo de Dijkstra: Cidade com semáforos e ruas com velocidade máxima permitida. 
Busca apenas a partir do vértice de origem para os demais vértices do grafo.
"""

import heapq

def dijkstra(grafo, tempos, origem):
    distancias = {vertice: float('inf') for vertice in grafo}
    caminho = {vertice: None for vertice in grafo}
    distancias[origem] = 0
    heap = [(0, origem)]
    
    while heap:
        tempo_atual, vertice_atual = heapq.heappop(heap)

        for vizinho, (distancia, v_max) in grafo[vertice_atual].items():
            tempo_viagem = distancia / v_max
            novo_tempo = tempo_atual + tempo_viagem
            
            while novo_tempo in tempos[vizinho]:
                novo_tempo += 1
            
            if novo_tempo < distancias[vizinho]:
                distancias[vizinho] = novo_tempo
                caminho[vizinho] = vertice_atual
                heapq.heappush(heap, (novo_tempo, vizinho))
    
    return {v: {"distancia": distancias[v], "pai": caminho[v]} for v in grafo}

def reconstruir_caminho(resultado, destino):
    if resultado[destino]["distancia"] == float('inf') or resultado["destino"]["pai"] == None:
        return None
    
    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = resultado[atual]["pai"]
    return caminho[::-1]

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

grafo = dijkstra(grafo, tempos, "1")
print(f"Caminho de 1 a {n}: {' -> '.join(reconstruir_caminho(grafo, n))}")