year = int(input("Введите год : "))
if 1900 < year < 100000:
    print("Correct year")
    if year % 400 == 0:
        print(year, "is leap year!")
    elif year % 100 == 0:
        print(year, "is not leap year!")
    elif year % 4 == 0:
        print(year, "is leap year!")
else:
    print("Write correct year")