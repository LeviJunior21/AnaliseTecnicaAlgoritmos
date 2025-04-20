def binomial(n, k):
    matriz = [[0] * (k + 1) for _ in range(n + 1)]

    for linha_i in range(0, len(matriz)):
        for coluna_i in range(0, min(linha_i + 1, k + 1)):
            print(linha_i, coluna_i)
            if (coluna_i == 0 or linha_i == coluna_i):
                matriz[linha_i][coluna_i] = 1
            else:
                matriz[linha_i][coluna_i] = matriz[linha_i - 1][coluna_i - 1] + matriz[linha_i - 1][coluna_i]

    print(matriz)
    return matriz[linha_i][coluna_i]

print(binomial(4,3))