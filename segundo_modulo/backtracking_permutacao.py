"""
backtrack(X[1..i])
    if X[1..i] == solução:
        write X[1..i]
    else:
        for each x E A(i+1):
            X[i + 1] = x
            backtrack(X[1..i + 1])
"""

#Backtracking via força bruta"
def permutacao(array, resultado, i):
    if i == len(array):
        print(resultado)
    else:
        for j in range(len(array)):
            resultado[i] = array[j]
            permutacao(array, resultado, i + 1)

permutacao([1,2,3], [None, None, None], 0)

#Poda
def permutacao(array, resultado, i):
    if i == len(array):
        print(resultado)
    else:
        for j in range(len(array)):
            resultado[i] = array[j]
            permutacao(array, resultado, i + 1)

permutacao([1,2,3], [None, None, None], 0)