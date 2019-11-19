import sys


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)
print(sys.getrecursionlimit())
print(fib(1400))
