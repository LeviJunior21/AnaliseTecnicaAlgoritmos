def sort(array):
    for i in range(len(array) - 1):
        menor = i
        for j in range(i + 1, len(array)):
            if array[j] < array[menor]:
                menor = j
        
        menor_anterior = array[i]
        array[i] = array[menor]
        array[menor] = menor_anterior

array = [9,8,7,6,5,4,3,2,1,0]
sort(array)
print(array)