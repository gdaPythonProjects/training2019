import math

x = int(input("podaj liczbe do zbadania"))

prime = True

if x < 2:
    prime = False
else:
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            prime = False
            break

if prime:
    print("Jest pierwsza")
else:
    print("Jest złożona")
