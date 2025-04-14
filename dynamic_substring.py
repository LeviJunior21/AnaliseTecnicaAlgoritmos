def buscar_ocorrencias(palavra: str, texto: str):
    posicoes = []

    if (len(texto) >= len(palavra)):
        matriz = [([0] * (len(palavra) + 1)) for _ in range(len(texto) + 1)] 
        maior = -1
        
        for linha_i in range(1, len(matriz)):
            for coluna_i in range(1, len(matriz[linha_i])):
                if palavra[coluna_i - 1] == texto[linha_i - 1]:
                    valor = 1 + matriz[linha_i - 1][coluna_i - 1]
                    matriz[linha_i][coluna_i] = valor
                    
                    inicio_palavra = (linha_i - 1) - len(palavra) + 1
                    fim_palavra = linha_i - 1
                    
                    if fim_palavra - inicio_palavra == len(palavra) - 1:
                        if (valor > maior):
                            posicoes = [[inicio_palavra, fim_palavra]]
                            maior = valor
                        elif (valor >= maior):
                            posicoes.append([inicio_palavra, fim_palavra])
    return posicoes

def realizar_teste(testes):
    for teste in testes:
        posicoes = buscar_ocorrencias(texto=teste[0], palavra=teste[1])
        print(len(posicoes))
    
testes = []
# 1. Texto muito longo com palavra no início
testes.append(["a" * 10**6 + "abc", "abc"])
# 2. Texto muito longo com palavra no fim
testes.append(["x" * (10**6) + "xyz", "xyz"])
# 3. Palavra repetida ao longo do texto de forma espaçada
testes.append(["abcdefg" * 1000, "efg"])  # "efg" aparece a cada 7 caracteres
# 4. Texto inteiro composto apenas pela palavra repetida
testes.append(["abc" * 1000, "abc"])  # Deve encontrar 1000 ocorrências
# 5. Teste com sobreposição (palavra menor que repete continuamente)
testes.append(["aaaaaaa", "aaa"])  # Sobreposição de "aaa"
# 6. Palavra maior que o texto
testes.append(["short", "thisisaverylongword"])  # Nenhuma ocorrência
# 7. Texto e palavra são idênticos
testes.append(["abcdefgh", "abcdefgh"])  # Apenas uma ocorrência
# 8. Texto gigante sem a palavra
testes.append(["a" * (10**6), "xyz"])  # Nenhuma ocorrência
# 9. Palavra com caracteres especiais
testes.append(["ab#cd$ef@gh", "#cd$"])  # Teste com caracteres especiais
# 10. Texto e palavra vazios (caso extremo)
testes.append(["", ""])  # Deve retornar nenhuma ocorrência

for teste in testes:
    posicoes = buscar_ocorrencias(texto=teste[0], palavra=teste[1])

    print(len(posicoes))
