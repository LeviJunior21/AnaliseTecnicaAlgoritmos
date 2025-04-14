def cassino(ganhos):
    ganhos_acumulados = [0] * len(ganhos)
    
    for i in range(0, len(ganhos)):
        ganhos_acumulados[i] = ganhos[i]
        if (ganhos_acumulados[i - 1] >= 0):
            ganhos_acumulados[i] += ganhos_acumulados[i - 1]
        
    max_ganho = ganhos_acumulados[0]
    for ganho_i in range(1, len(ganhos_acumulados)):
        if (ganhos_acumulados[ganho_i] > max_ganho):
            max_ganho = ganhos_acumulados[ganho_i]
    
    print(ganhos_acumulados)
    return max_ganho

ganhos = [20, -30, 15, -10, 30, -20, -30, 30]
maximo = cassino(ganhos)
print(maximo)