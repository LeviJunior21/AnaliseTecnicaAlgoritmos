maior_valor = 0
melhor_comb = []
def backtrack(mochila, itens, capacidade, peso_total, valor_total, i, j):
    global maior_valor, melhor_comb
    if peso_total <= capacidade:
        if len(mochila) == i or j == len(mochila):
            if valor_total > maior_valor:
                maior_valor = valor_total
                melhor_comb = mochila.copy()
        else:
            mochila_com = mochila.copy()
            mochila_com[j] = itens[j]
            backtrack(mochila_com, itens, capacidade, peso_total + itens[j][0], valor_total + itens[j][1], i + 1, j + 1)
            backtrack(mochila.copy(), itens, capacidade, peso_total, valor_total, i, j + 1)

itens = [[15, 20], [5, 30], [10, 50], [5, 10]]
mochila = [0] * len(itens)
backtrack(mochila, itens, 16, 0, 0, 0, 0)
print(melhor_comb)

maior_valor = 0
melhor_comb = []
def backtrack(mochila, itens, capacidade, valor, i):
    global maior_valor, melhor_comb
    if i == len(itens):
        if valor > maior_valor:
            maior_valor = valor
            melhor_comb = mochila.copy()
    else:
        if itens[i][0] <= capacidade:
            mochila[i] = itens[i] # mochila[i] = 1
            backtrack(mochila, itens, capacidade - itens[i][0], valor + itens[i][1], i + 1)
        mochila[i] = 0
        backtrack(mochila, itens, capacidade, valor, i + 1)
        
backtrack(mochila, itens, 16, 0, 0)
print(melhor_comb)
