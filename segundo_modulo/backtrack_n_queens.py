def n_queens(tabuleiro, i):
    if i == len(tabuleiro) + 1:
        print(tabuleiro)
    else:
        for j in range(len(tabuleiro)):
            tabuleiro[i] = j
            if valid(tabuleiro, i):
                n_queens(tabuleiro, i + 1)

def valid(tabuleiro, i):
    for j in range(i):
        if tabuleiro[i] == tabuleiro[j] or abs(tabuleiro[i] - tabuleiro[j]) == abs(i - j):
            return False
    return True

n = 8
tabuleiro = [0] * n
n_queens(tabuleiro, 0)
