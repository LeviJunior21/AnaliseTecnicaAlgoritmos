"""
Ordenação topológica: Aula. 
"""

grafo = {"7": ["11", "8"], "11": ["2", "9", "10"], "3": ["8", "10"], "5": ["11"], "2": [], "9": [], "10": [], "8": []}

def visitaDFS_branco(grafo, vertice, cor, pais, inicio, fim, tempo, lista):
    cor[vertice] = "CINZA"
    tempo[0] += 1
    inicio[vertice] = tempo[0]
    
    for vertice_i in grafo[vertice]:
        if cor[vertice_i] == "BRANCO":
            pais[vertice_i] = vertice
            visitaDFS_branco(grafo, vertice_i, cor, pais, inicio, fim, tempo, lista)
    
    cor[vertice] = "PRETO"
    tempo[0] += 1
    fim[vertice] = tempo[0]
    lista.insert(0, vertice)

def dfs(grafo):
    cor= {}
    pais = {}
    inicio = {}
    fim = {}
    tempo = [0]
    lista = []
    
    for vertice in grafo:
        cor[vertice] = "BRANCO"
        pais[vertice] = None
    
    for vertice in grafo:
        if cor[vertice] == "BRANCO":
            visitaDFS_branco(grafo, vertice, cor, pais, inicio, fim, tempo, lista)

    return cor, pais, inicio, fim, lista

cor, pais, inicio, fim, lista = dfs(grafo, "7")
print("Lista:", " -> ".join(lista))