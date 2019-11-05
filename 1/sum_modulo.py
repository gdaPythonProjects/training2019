x = int(input("Podaj liczbę\n"))
even = 0
odd = 0
for i in range(x+1):
    if i % 2 == 0:
        even += i
    else:
        odd += i
print("Suma liczb parzystych: ", even)
print("Suma liczb NIEparzystych: ", odd)
