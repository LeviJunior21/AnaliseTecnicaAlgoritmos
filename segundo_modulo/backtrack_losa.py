def backtrack(array, i, j):
    if i == 0 or j == 0:
        return 0
    if array[i] == array[j]:
        return backtrack(array, i - 1, j - 1)
    else:
        return max(backtrack(array, i - 1, j), backtrack(array, i, j - 1))