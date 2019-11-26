def add_values(x, y):
    return x + y


print(add_values(2, 7))
a = (1, 10)
print(add_values(a[0], a[1]))
print(add_values(*a))

b = [5, 2]
print(add_values(*b))

dictionary_values = {
    'x': 1,
    'y': 2
}

print(add_values(**dictionary_values))


def printer(*param):
    for i in param:
        print(i)


printer(["Akacja", "Wiśnia", "Czereśnia"])
