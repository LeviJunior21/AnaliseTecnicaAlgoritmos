def escadas(degraus: int) -> int:
    degraus_mais_longo = [0] * degraus + [0]
    
    for i in range(degraus + 1):
        if (i <= 1):
            degraus_mais_longo[i] = i + 1
        else:
            degraus_mais_longo[i] = degraus_mais_longo[i - 1] + degraus_mais_longo[i - 2]
            
    return degraus_mais_longo[-1]

degraus = 4
resultado = escadas(degraus=degraus)
print(resultado)