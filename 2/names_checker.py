names = []


def check_name(name):
    return name in names


t = int(input("Ile imion chcesz podac?\n"))
while t:
    names.append(input("Podaj imię: "))
    t -= 1
print(check_name("Marcin"))
print(check_name("Ala"))
