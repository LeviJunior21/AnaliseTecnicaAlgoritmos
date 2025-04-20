import heapq, math

def dijkstra(grafo, origem, destino, semaforos):
    pai = {vertice: None for vertice in grafo}
    custo = {vertice: math.inf for vertice in grafo}
    
    heap = [(0, origem)]
    custo[origem] = 0
    visitados = set()
    
    while heap:
        custo_atual, vertice_atual = heapq.heappop(heap)
        if vertice_atual == destino: 
            break
        if vertice_atual in visitados:
            continue
        visitados.add(vertice_atual)
        
        for vertice_adj, custo_aresta_ate_adj in grafo[vertice_atual].items():
            novo_custo_adj = custo_atual + custo_aresta_ate_adj
            
            if vertice_adj in semaforos and novo_custo_adj in semaforos[vertice_adj]:
                novo_custo_adj += 1
            
            if novo_custo_adj < custo[vertice_adj]:
                custo[vertice_adj] = novo_custo_adj
                pai[vertice_adj] = vertice_atual
                heapq.heappush(heap, (novo_custo_adj, vertice_adj))
    
    lista = []
    atual = destino
    while atual:
        lista.append(atual)
        atual = pai[atual]
    
    return lista[::-1], custo[destino]


def prim(grafo, origem):
    heap = [(0, origem)]
    visitados = set()
    pai = {vertice: None for vertice in grafo}
    custo = {vertice: math.inf for vertice in grafo}
    
    custo_total = 0
    total_visitados = 0
    
    while heap:
        custo_aresta_atual, vertice_atual = heapq.heappop(heap)
        
        if vertice_atual in visitados:
            continue
        visitados.add(vertice_atual)
        
        custo_total += custo_aresta_atual
        total_visitados += 1
        
        for vertice_adj, custo_aresta_ate_adj in grafo[vertice_atual].items():
            if vertice_adj not in visitados and custo_aresta_ate_adj < custo[vertice_adj]:
                custo[vertice_adj] = custo_aresta_ate_adj
                pai[vertice_adj] = vertice_atual
                heapq.heappush(heap, (custo_aresta_ate_adj, vertice_adj))
    
    if total_visitados == len(grafo):
        return custo_total, pai
    else:
        return -1, None



grafo = {}

vertices, arestas, origem = map(int, input().split())
for i in range(vertices):
    grafo[str(i + 1)] = {}

for _ in range(arestas):
    u, v, w = input().split()
    grafo[u][v] = int(w)
    grafo[v][u] = int(w)

semaforos = {"2": [3], "3": [3, 4]}
semaforos = {"2": [3]}
lista = []
solucao = dijkstra(grafo, str(origem), str(vertices), semaforos)
for vertice in solucao[0]:
    lista.append(vertice)
print(" -> ".join(lista), solucao[1])

lista = []
for origem in grafo:
    total, caminho = prim(grafo, str(origem))
    lista.append(total)
print(min(lista))
