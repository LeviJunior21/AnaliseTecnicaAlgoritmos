"""
Uma escola está organizando um evento e possui n alunos, numerados de 1 a n.
Cada aluno pode ter um mentor que é um outro aluno, ou pode não ter um mentor,
caso em que será considerado um aluno independente. Um aluno A é considerado
o mentor de um aluno B se uma das seguintes condições for verdadeira.

Entrada: 5 -1  1  2  1  -1
Saida: 3
"""

import sys
sys.setrecursionlimit(3000)

n = int(input())
mentores = [int(input()) for _ in range(n)]
def profundidade(i):
    if mentores[i] == -1:
        return 1
    if memo[i] != -1:
        return memo[i]
    memo[i] = 1 + profundidade(mentores[i] - 1)
    return memo[i]
memo = [-1] * n
resposta = 0

for i in range(n):
    resposta = max(resposta, profundidade(i))
print(resposta)

def calcular_profundidade(i, p, memo):
    if memo[i] != 0:
        return memo[i]
    if p[i] == -1:
        memo[i] = 1
    else:
        memo[i] = 1 + calcular_profundidade(p[i] - 1, p, memo)
    return memo[i]

n = int(input())
p = [int(input()) for _ in range(n)]

memo = [0] * n
max_grupos = 0

for i in range(n):
    max_grupos = max(max_grupos, calcular_profundidade(i, p, memo))
print(max_grupos)

n = int(input())
p = [int(input()) for _ in range(n)]
grafo = [[] for _ in range(n)]

for i in range(n):
    if p[i] != -1:
        grafo[p[i] - 1].append(i)

def dfs(v):
    if not grafo[v]:
        return 1
    return 1 + max(dfs(u) for u in grafo[v])

max_profundidade = 0
for i in range(n):
    if p[i] == -1:
        max_profundidade = max(max_profundidade, dfs(i))
print(max_profundidade)

n = int(input())
p = [int(input()) for _ in range(n)]
grafo = [[] for _ in range(n)]

for i in range(n):
    if p[i] != -1:
        grafo[p[i] - 1].append(i)
def dfs(v):
    max_prof = 1 
    for vizinho in grafo[v]:
        max_prof = max(max_prof, 1 + dfs(vizinho))
    return max_prof
profundidade_maxima = 0
for i in range(n):
    if p[i] == -1:
        profundidade_maxima = max(profundidade_maxima, dfs(i))

print(profundidade_maxima)
