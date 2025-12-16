from functools import total_ordering
def fib(n):
    if n==0:
        return 1
    elif n==1:
        return 1

    return fib (n-1) + fib (n-2)
    for i in range (40):
        print(fib(i))