def ssdc(A, n):
    c = [0] * n 
    for m in range(n):
        c[m] = 1
        for i in range(m - 1, 0, -1):
            if A[i] <= A[m] and c[i] + 1 > c[m]:
                c[m] = c[i] + 1
    return c
 
A = [40, 11, 90, 22, 33, 50, 60, 44, 70, 55]
resultado = ssdc(A, len(A))
print(resultado)