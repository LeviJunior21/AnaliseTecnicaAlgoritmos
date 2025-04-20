def roubar(pesos, precos, peso_total):
    itens = [[pesos[i], precos[i], pesos[i]/precos[i]] for i in range(len(pesos))]
    itens.sort(key=lambda x: x[2])
    
    soma_pesos = 0
    escolhidos = []
    
    while peso_total != soma_pesos and itens:
        peso_atual = soma_pesos + itens[-1][0]
        if peso_atual <= peso_total:
            soma_pesos += itens[-1][0]
            escolhidos.append([itens[-1][0], itens[-1][1]])

        itens.pop(-1)
    
    return escolhidos

itens = [8, 5, 5]
precos = [9, 5, 5]
w = 10
print(roubar(itens, precos, w))