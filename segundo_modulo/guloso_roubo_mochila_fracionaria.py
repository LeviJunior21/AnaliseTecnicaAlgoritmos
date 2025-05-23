def roubar(pesos, precos, peso_total):
    itens = [[pesos[i], precos[i], pesos[i]/precos[i]] for i in range(len(pesos))]
    itens.sort(key=lambda x: x[2], reverse=True)
    
    soma_pesos = 0
    escolhidos = []
    
    while peso_total != soma_pesos and itens:
        peso_atual = soma_pesos + itens[-1][0]
        if peso_atual <= peso_total:
            soma_pesos += itens[-1][0]
            escolhidos.append([itens[-1][0], itens[-1][1]])
        else:
            peso = (peso_total - soma_pesos)/itens[-1][0]
            soma_pesos += peso
            escolhidos.append([float(f"{peso:.2f}"), float(f"{peso * itens[-1][1]:.2f}")])
            
        itens.pop(-1)
    
    return escolhidos

pesos = [10, 20, 45]
precos = [70, 80, 120]
w = 50
print(roubar(pesos, precos, w))