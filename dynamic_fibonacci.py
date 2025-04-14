def fibonacci(n: int):
    memoria = [None] * (n + 1)
    return fib(n, memoria=memoria)

def fib(n: int, memoria) -> int:
    if n == 0 or n == 1: return n    
    if (memoria[n] == None):
        return fibonacci(n - 1) + fibonacci(n - 2)
    return memoria[n]

resultado = fibonacci(6)
print(resultado)