def week_day(zday):
    day = zday.lower()
    if day == "poniedziałek":
        return 1
    elif day == "wtorek":
        return 2
    elif day == "środa":
        return 3
    elif day == "czwartek":
        return 4
    elif day == "piątek":
        return 5
    elif day == "sobota":
        return 6
    elif day == "niedziela":
        return 7
    return 0


t = int(input("Podaj ilość przypadków: "))
while t:
    day = input("Podaj dzień: ")
    day_number = week_day(day)
    if day_number:
        print(day_number)
    else:
        print("No niestety, ale nie ma takiego dnia...")
    t -= 1
