def substring_maxima(valores):
    maximos = [0] * len(valores)
    
    for inicio in range(len(valores) -1, -1, -1):
        candidatos = [0]

        for i in range(inicio + 1, len(valores)):
            if valores[i] >= valores[inicio]:
                candidatos.append(maximos[i])
        
        maximos[inicio] = 1 + max(candidatos)
    
    return maximos

valores = [9, 5, 6, 3, 9, 6, 4, 7]
valores = [40, 11, 90, 22, 33, 50, 60, 44, 70, 55]
resultado = substring_maxima(valores)
print(resultado)
print(max(resultado))