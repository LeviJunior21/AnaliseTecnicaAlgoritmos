"""Minimizar o troco retornado com o número mínimo de moedas"""

def calcula_troco(moedas, total):
    soma = 0
    conjunto = []
    while soma != total and moedas:
        if soma + moedas[0] > total:
            moedas.pop(0)
        else:
            soma += moedas[0]
            conjunto.append(moedas[0])
    
    return conjunto

moedas = [1, 0.25, 0.10, 0.05]
total = 2.89
print(calcula_troco(moedas, total))