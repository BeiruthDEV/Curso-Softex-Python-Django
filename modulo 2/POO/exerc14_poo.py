def fibonacci(n):
    if n <= 0:
        return []
    sequencia = [0]
    if n == 1:
        return sequencia
    sequencia.append(1)
    while len(sequencia) < n:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

print(fibonacci(10))
