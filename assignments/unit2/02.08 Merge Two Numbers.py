x = int(input("Please enter a two digit number: "))

y = int(input("Please enter another two digit number: "))

print("Merged Number:","{:<1d}{:<1d}{:<1d}{:<1d}".format(x // 10, y // 10, x % 10, y % 10))