import heapq

def conecta(grafo, n):
    visitado = [False] * (n + 1)
    min_heap = [(0, 1)] # Começa do vértice 1 com custo 0
    total_custo = 0
    arestas_usadas = 0
    
    while min_heap:
        custo, u = heapq.heappop(min_heap)
        
        if visitado[u]:
            continue
        
        visitado[u] = True
        total_custo += custo
        arestas_usadas += 1
        
        for v, peso in grafo[u]:
            if not visitado[v]:
                heapq.heappush(min_heap, (peso, v))
        
        if arestas_usadas == n:
            break
    
    return total_custo if arestas_usadas == n else "IMPOSSIBLE"

n, m = map(int, input().split())
grafo = [[] for _ in range(n + 1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    grafo[a].append((b, c))
    grafo[b].append((a, c))

print(conecta(grafo, n))