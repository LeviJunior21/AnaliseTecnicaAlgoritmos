def ordenacao_topologica():
    n, m = map(int, input().split())
    grafo = [[] for _ in range(n + 1)]
    grau_entrada = [0] * (n + 1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        grafo[a].append(b)
        grau_entrada[b] += 1
    
    fila = []
    for i in range(1, n + 1):
        if grau_entrada[i] == 0:
            fila.append(i)
    
    ordem = []
    inicio = 0
    
    while inicio < len(fila):
        u = fila[inicio]
        inicio += 1
        ordem.append(u)
        
        for v in grafo[u]:
            grau_entrada[v] -= 1
            if grau_entrada[v] == 0:
                fila.append(v)
    
    
    if len(ordem) == n:
        print(" ".join(str(x) for x in ordem))
    else:
        print("IMPOSSIBLE")

ordenacao_topologica()