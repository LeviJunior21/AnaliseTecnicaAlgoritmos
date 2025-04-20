def subset(cheques, valor):
    resultado = False
    matriz = [[0] * (valor + 1) for _ in range(len(cheques) + 1)]
        
    for valor_a_pagar_i in range(1, len(matriz)):
        for valor_pago_i in range(1, len(matriz[0])):
            if (cheques[valor_a_pagar_i - 1] == valor_pago_i):
                matriz[valor_a_pagar_i][valor_pago_i] = max(cheques[valor_a_pagar_i - 1], matriz[valor_a_pagar_i - 1][valor_pago_i])
            elif (cheques[valor_a_pagar_i - 1] > valor_pago_i):
                matriz[valor_a_pagar_i][valor_pago_i] = matriz[valor_a_pagar_i - 1][valor_pago_i]
            else:
                diferenca = valor_pago_i - cheques[valor_a_pagar_i - 1]
                matriz[valor_a_pagar_i][valor_pago_i] = max(cheques[valor_a_pagar_i - 1] + matriz[valor_a_pagar_i - 1][diferenca], matriz[valor_a_pagar_i - 1][valor_pago_i])
                
    if (matriz[-1][-1] == valor): 
        resultado = True
        
    return resultado

cheques = [1, 3, 5, 8]
valor = 15
resultado = subset(cheques=cheques, valor=valor)
print(resultado)