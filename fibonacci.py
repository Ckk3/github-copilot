# Sequencia de fibbonaci
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(10))
print(10+9+8+7+6+5+4+3+2+1)