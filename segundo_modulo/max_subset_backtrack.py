def backtrack(itens, pesos, escolhidos, qtde_itens, soma_pesos, t, i, j):
    if soma_pesos == t:
        return escolhidos, qtde_itens
    elif soma_pesos > t or i >= len(itens) or j >= len(itens):
        return None, qtde_itens
    else:
        qtde_itens_melhor = qtde_itens
        melhor_escolha = escolhidos
        for i in range(i, len(pesos)):
            copia_escolhidos = escolhidos.copy()
            copia_escolhidos.append(itens[j])
            
            escolhidos_momento, qtde_itens_momento = backtrack(itens, pesos, copia_escolhidos, qtde_itens + 1, soma_pesos + pesos[j], t, i + 1, j + 1)
            if escolhidos_momento is not None and qtde_itens_momento > qtde_itens_melhor:
                qtde_itens_melhor = qtde_itens_momento
                melhor_escolha = escolhidos_momento
            
            escolhidos_momento, qtde_itens_momento = backtrack(itens, pesos, escolhidos, qtde_itens, soma_pesos, t, i, j + 1)
            if escolhidos_momento is not None and qtde_itens_momento > qtde_itens_melhor:
                qtde_itens_melhor = qtde_itens_momento
                melhor_escolha = escolhidos_momento
    
    return melhor_escolha, qtde_itens_melhor

def max_sum_elements(itens, pesos, t):
    escolha, qtd = backtrack(itens=itens, pesos=pesos, escolhidos=[], qtde_itens=0, soma_pesos=0, t=t, i=0, j=0)
    if qtd == t:
        return escolha, qtd
    return None, float('inf')

itens = [1, 2, 3, 4, 10, 20, 30, 40]
pesos = [1, 1, 2, 1, 10, 20, 30, 1]
t = 4

print(max_sum_elements(itens, pesos, t))