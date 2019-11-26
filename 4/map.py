from math import sqrt


def int_sqrt(value):
    return int(sqrt(value))


number = [1, 7, 14, 21]
x = []
for i in number:
    x.append(int_sqrt(i))

y = [int_sqrt(i) for i in number]

print(x)
print(y)

# map!:

print(list(map(int_sqrt, number)))

