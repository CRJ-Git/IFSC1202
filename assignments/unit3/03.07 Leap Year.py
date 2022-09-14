year = int(input("Please enter a 4 digit year: "))

if (year / 4) % 1 == 0 and (year / 100) % 1 != 0:
    print("LEAP YEAR")
elif (year / 400) % 1 == 0:
    print("LEAP YEAR")
else:
    print("COMMON YEAR")