def backtrack(conjunto, subconjunto, d, soma, i, j):
    if d == soma:
        print(subconjunto)
    else:
        if i == len(conjunto) or j == len(conjunto):
            if d == soma:
                print(subconjunto)
        else:
            new_subconjunto = subconjunto.copy()
            new_subconjunto[i] = conjunto[j]
            backtrack(conjunto, new_subconjunto, d, soma + conjunto[j], i + 1, j + 1)
            backtrack(conjunto, subconjunto, d, soma, i, j + 1)

conjunto = [1,2,5,6,8]
subconjunto = [None] * len(conjunto) 
d = 9

backtrack(conjunto, subconjunto, d, 0, 0, 0)