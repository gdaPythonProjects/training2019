import math


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


t = int(input("Ile liczb chcesz sprawdzic?"))
while t:
    x = int(input("Podaj liczbe do sprawdzenia"))
    if is_prime(x):
        print(x, " jest pierwsze")
    else:
        print(x, " jest złożone")
    t -= 1
