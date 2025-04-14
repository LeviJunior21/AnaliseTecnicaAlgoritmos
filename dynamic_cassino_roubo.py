def cassino_roubo(lista: list) -> int:    
    roubo_momento = [0] * len(lista)
    
    for i in range(len(lista) - 1, -1, -1):
        valor = lista[i]
        if (i == len(lista) - 1 or i == len(lista) - 2):
            roubo_momento[i] = valor
        else:
            roubo_momento[i] = valor + max(roubo_momento[i + 2:])
    
    return max(roubo_momento)

lista = [2, 7, 9, 3, 1]
resposta = cassino_roubo(lista=lista)
print(resposta)