ip = "10.120.24.23"
x = ip.split(".")
print(type(x))
print(x)

y = []
for i in x:
    y.append(int(i))
print(y)

z = [int(i) for i in x]
print(z)

a = [int(i) for i in x if int(i) % 2 == 0]
print(a)
