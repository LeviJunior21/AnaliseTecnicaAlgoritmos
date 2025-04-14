def mochila(itens, capacidade):
    numero_linhas = len(itens) + 1
    matriz = [[0] * (capacidade + 1) for _ in range(numero_linhas)]
    
    for linha_i in range(1, numero_linhas):
        peso, valor = itens[linha_i - 1]

        for capacidade_atual in range(1, capacidade + 1):
            if (peso > capacidade_atual):
                matriz[linha_i][capacidade_atual] = matriz[linha_i - 1][capacidade_atual]
            else:
                coluna_resto = capacidade_atual - peso
                matriz[linha_i][capacidade_atual] = max(valor + matriz[linha_i - 1][coluna_resto], matriz[linha_i - 1][capacidade_atual])

    return matriz[-1][-1]


def itens_escolhidos(matriz, itens):
    itens_usados = []
    linha, coluna = len(matriz) - 1, len(matriz[-1]) - 1
    
    while linha > 0 and coluna > 0:
        if (matriz[linha][coluna] != matriz[linha - 1][coluna]):
            itens_usados.append(itens[linha - 1][0])
            coluna -= itens[linha - 1][0]
        linha -= 1
    
    return itens_usados[::-1]


itens = [[1,1],[3,5],[5,8],[8,10]]
capacidade = 11
resultado, matriz = mochila(itens, capacidade)
itens_usados = itens_escolhidos(matriz, itens)

print(f"Os itens usados foram: {itens_usados} e o valor da mochila é {resultado}.")


itens = [[4,400],[2,400],[1,300],[3,450]]
capacidade = 5
resultado, matriz = mochila(itens, capacidade)
itens_usados = itens_escolhidos(matriz, itens)

print(f"Os itens usados foram: {itens_usados} e o valor da mochila é {resultado}.")


n, capacidade = input().split(" ")
itens = []
for _ in range(int(n)):
    peso, valor = input().split(" ")
    itens.append([int(peso), int(valor)])

resultado = mochila(itens, int(capacidade))
print(resultado)