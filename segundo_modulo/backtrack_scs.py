def scs(array_a, array_b, i, j):
    if i == 0:
        return j
    if j == 0:
        return i
    if array_a[i - 1] == array_b[j - 1]:
        return 1 + scs(array_a, array_b, i - 1, j - 1)
    else:
        return 1 + min(scs(array_a, array_b, i, j - 1), scs(array_a, array_b, i - 1, j))

array_a = ['K', 'L', 'M', 'N', 'O', 'P']
array_b = ['A', 'L', 'X', 'O', 'P', 'Q']
i = len(array_a)
j = len(array_b)
print(scs(array_a, array_b, i, j))