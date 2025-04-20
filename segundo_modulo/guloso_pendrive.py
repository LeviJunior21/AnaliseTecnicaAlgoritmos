def pendrive(arquivos, armazenamento, result):
    arquivos_ordenados = sorted(arquivos, key=lambda x: x, reverse=False)
    
    i = 0
    while (i < len(arquivos_ordenados) and armazenamento > 0):
        arquivo = arquivos_ordenados[i]
        if arquivo <= armazenamento:
            result.append(arquivo)
            armazenamento -= arquivo
        
        i += 1

arquivos = [10, 15, 20, 20, 30, 35, 40, 50, 10]
gravados = 90
result = []
pendrive(arquivos, gravados, result)

print(result)