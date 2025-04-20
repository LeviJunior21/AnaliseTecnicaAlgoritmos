def lcs(array_a, array_b, i, j):
    if i == 0 or j == 0:
        return 0
    if array_a[i - 1] == array_b[j - 1]:
        return 1 + lcs(array_a, array_b, i - 1, j - 1)
    else:
        return max(lcs(array_a, array_b, i, j - 1), lcs(array_a, array_b, i - 1, j))

array_a = ['A', 'B', 'C', 'D', 'G', 'H']
array_b = ['A', 'E', 'D', 'F', 'H', 'R']
i = len(array_a)
j = len(array_b)
print(lcs(array_a, array_b, i, j))

def lcs(array_a, array_b, i, j):
    if i == 0 or j == 0:
        return 0, []
    if array_a[i - 1] == array_b[j - 1]:
        tamanho, subseq = lcs(array_a, array_b, i - 1, j - 1)
        return 1 + tamanho, subseq + [array_a[i - 1]]
    else:
        tamanho1, subseq1 = lcs(array_a, array_b, i, j - 1) 
        tamanho2, subseq2 = lcs(array_a, array_b, i - 1, j)
        if tamanho1 > tamanho2:
            return tamanho1, subseq1
        return tamanho2, subseq2

array_a = ['A', 'B', 'C', 'D', 'G', 'H']
array_b = ['A', 'E', 'D', 'F', 'H', 'R']
i = len(array_a)
j = len(array_b)
print(lcs(array_a, array_b, i, j))