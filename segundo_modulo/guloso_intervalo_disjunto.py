def max_guloso(a, b, p, r):
    x = [p]
    k = p
    for i in range(p + 1, r):
        if a[i] > b[k]:
            x.append(i)
            k = i
    return x

a = [6, 25, 9, 23, 7, 18, 30, 1]
b = [15, 30, 15, 28, 16, 24, 34, 26]

print(max_guloso(a, b, 0, len(a)))