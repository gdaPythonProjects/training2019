numbers = [1, 2, 8, 4]


def multiply_two(lst):
    for num in lst:
        yield num * 2


result = multiply_two(numbers)
print(next(result))
print(next(result))
print(next(result))
print(next(result))

result = multiply_two(numbers)
print(list(result))

result = multiply_two(numbers)
for i in result:
    print(i)

