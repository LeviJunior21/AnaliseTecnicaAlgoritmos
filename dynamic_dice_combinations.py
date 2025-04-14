def dice_combinations1(n):
    array = [0] * n
    
    for i in range(n):
        if (i <= 5):
            array[i] = 2 ** i
        else:
            for j in range(i, i - 7, - 1):
                array[i] += array[j] % (10 ** 9 + 7)
    
    return array[-1] 

def dice_combinations2(n):
    array = [0] * n
    
    for i in range(n):
        if (i <= 5):
            array[i] = 2 ** i
        else:
            array[i] = (array[i - 1] + array[i - 2] + array[i - 3] + array[i - 4] + array[i - 5] + array[i - 6]) % (10 ** 9 + 7)

    return array[-1]
    
n = int(input())
resultado = dice_combinations2(n)
print(resultado)
