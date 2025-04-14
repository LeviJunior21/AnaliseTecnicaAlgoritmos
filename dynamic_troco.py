def troco_com_reposicao(moedas, troco):
    matriz = [([0] * (troco + 1)) for _ in range(len(moedas) + 1)]
    for i in range(len(matriz[0])):
        matriz[1][i] = i
    
    for moeda_i in range(2, len(matriz)):
        for troco_i in range(1, len(matriz[moeda_i])):
            if (moedas[moeda_i - 1] > troco_i):
                matriz[moeda_i][troco_i] = matriz[moeda_i - 1][troco_i]
            else:
                matriz[moeda_i][troco_i] = min(matriz[moeda_i - 1][troco_i], matriz[moeda_i][troco_i - moedas[moeda_i - 1]] + 1)
    return matriz

def moedas_usadas(moedas, matriz):
    linha, coluna = len(matriz) - 1, len(matriz[0]) - 1  
    moedas_usadas = []
    
    while True:
        if (linha == 0):
            break
        if (matriz[linha - 1][coluna] == matriz[linha][coluna]):
            linha -= 1
        else:
            moedas_usadas.append(moedas[linha - 1])
            coluna = coluna - moedas[linha - 1]
    
    return moedas_usadas

moedas = [1,4,6]
troco = 15
trocos = troco_com_reposicao(moedas, troco)
moedas_usadas = [str(moeda) for moeda in moedas_usadas(moedas=moedas, matriz=trocos)]

for linha in trocos: print(linha)
print(f"São necessárias {trocos[len(trocos) -1][len(trocos[0]) -1]} moedas. São elas: {', '.join(moedas_usadas[:-1])} e {moedas_usadas[-1]}.")