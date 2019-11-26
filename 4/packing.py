from itertools import zip_longest

pets = ["dog", "cat", "turtle"]
names = ["Bazyli", "Stefan", "Tuptuś"]
colors = ["Black", "Black"]

for i in zip(pets, names):
    print(i)

for i in zip(pets, names, colors):
    print(i)

for i in zip_longest(pets, names, colors):
    print(i)
