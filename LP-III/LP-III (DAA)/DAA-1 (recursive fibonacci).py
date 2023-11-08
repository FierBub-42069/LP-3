def fibon_recu(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibon_recu(n-1) + fibon_recu(n-2)

n = 10
print(f"Fibonacci({n}) using recursive method: {fibon_recu(n)}")