year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, " This a Leap year")
else:
    print(year, " Not a Leap year")