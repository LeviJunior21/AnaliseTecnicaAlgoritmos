import heapq, math

def solucao(grafo, N, T, K, P):
    tempo_limite = T * 60
    dist = [math.inf] * (N + 1)
    dist[1] = 0
    heap = [(0, 1)]

    while heap:
        tempo_atual, u = heapq.heappop(heap)

        if tempo_atual > dist[u]:
            continue
        for v, w in grafo[u]:
            custo_trilha = w * 60
            pausa = K if v in pinheiros else 0
            novo_tempo = tempo_atual + custo_trilha + pausa

            if novo_tempo < dist[v]:
                dist[v] = novo_tempo
                heapq.heappush(heap, (novo_tempo, v))

    return dist[N] if dist[N] <= tempo_limite else -1

N, M, T, K, P = map(int, input().split())
pinheiros = set(map(int, input().split()))
trilhas = []
    
for _ in range(M):
    u, v, w = map(int, input().split())
    trilhas.append((u, v, w))

grafo = [[] for _ in range(N + 1)]
for u, v, w in trilhas:
    grafo[u].append((v, w))

print(solucao(grafo, N, T, K, P))