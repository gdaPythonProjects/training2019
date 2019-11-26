def is_odd(value):
    return value % 2


x = [9, 1, 5, 3, 6, 2, 6, 2, 5, 2, 8]

print(list(filter(is_odd, x)))
