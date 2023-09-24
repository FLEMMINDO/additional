def fib(n):
    fib1 = fib2 = 1
    n = int(n) - 2

    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1

    return fib2

print(fib(7))