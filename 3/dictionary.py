x = {"cat": ["stefan", "bubuś"],
     "dog": {"type": "pitbull",
             "name": "azor"
             },
     "worm": "mrówka"
     }

for i in x.items():
    print(i)

for i, j in x.items():
    print(i, j)

for i in x.keys():
    print(i)

for i in x.values():
    print(i)

print(x["cat"])
print(x.get("cat"))
print(x.get("cokolwiek"))
print(x.get("cokolwiek","Brak klucza"))

del x["dog"]
for i, j in x.items():
    print(i, j)

if "dog" in x:
    print("Jest z nami piesek", x.get("dog"))
else:
    print("Nie ma z nami piesków")

if "stefan" in x.values():
    print("JEST!")
