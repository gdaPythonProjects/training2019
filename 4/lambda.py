import math

a = lambda x: x * x

print(a(4))

b = lambda x, y: y - math.sqrt(x)
print(b(2, 4))

numbers = [1, 7, 14, 21]
print(list(map(lambda x: int(math.sqrt(x)), numbers)))

names = ["Henryk Sienkiewicz", "Adam Mickiewicz",
         "Władysław Reymont"]

print(sorted(names, key=lambda x: x.split(" ")[-1]))
