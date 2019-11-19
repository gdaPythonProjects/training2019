def week_day(zday):
    day = zday.lower()
    days = ["poniedziałek", "wtorek", "sroda", "czwartek", "piątek", "sobota", "niedziela"]
    return 0 if day not in days else days.index(day)+1


t = int(input("Podaj ilość przypadków: "))
while t:
    day = input("Podaj dzień: ")
    day_number = week_day(day)
    if day_number:
        print(day_number)
    else:
        print("No niestety, ale nie ma takiego dnia...")
    t -= 1
