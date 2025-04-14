"""
Ordenação Topológica: Ordenação topológica para disciplinas.
"""

grafo = {}

def visita(grafo, v, cor, lista, inicio, fim, tempo, pais, i, subgrafos):
    cor[v] = "CINZA"
    tempo[0] += 1
    inicio[v] = tempo[0]
    
    for adj in grafo[v]:
        if cor[adj] == "BRANCO":
            pais[adj] = v
            visita(grafo, adj, cor, lista, inicio, fim, tempo, pais, i, subgrafos)
        
        if cor[adj] == "CINZA":
            raise Exception("IMPOSSIBLE")

    cor[v] = "PRETO"
    tempo[0] += 1
    fim[v] = tempo[0]
    lista.append((tempo[0], v))
    subgrafos[str(i)].append((tempo[0], v))

def dfs(grafo, sem_vertice_entrada):
    cor = {}
    lista = []
    inicio = {}
    fim = {}
    pais = {}
    tempo = [0]
    subgrafos = {}
    
    for v in grafo:
        cor[v] = "BRANCO"
        pais[v] = None
    
    i = 0
    for v in sem_vertice_entrada:
        if cor[v] == "BRANCO":
            subgrafos[str(i)] = []
            visita(grafo, v, cor, lista, inicio, fim, tempo, pais, i, subgrafos)
            i += 1
    
    return subgrafos

m, n = input().split()
sem_vertice_entrada = set()

for i in range(1, int(m) + 1):
    grafo[str(i)] = []
    sem_vertice_entrada.add(str(i))

for _ in range(int(n)):
    x, y = input().split()
    grafo[x].append(y)
    sem_vertice_entrada.remove(y)

try:
    data = dfs(grafo=grafo, sem_vertice_entrada=sem_vertice_entrada)
    for i in data:
        data[i] = sorted(data[i], key=lambda x: x[0], reverse=True)

    lists = list(data.values())
    lists = sorted(data.values(), key=lambda sub: sub[0][0], reverse=True)
    
    maximo = max(len(lst) for lst in lists)
    result = []
    
    for i in range(maximo):
        for lst in lists:
            if i < len(lst):
                result.append(lst[i][1])
            
    print(" ".join(result))
except Exception as e:
    print("IMPOSSIBLE")
