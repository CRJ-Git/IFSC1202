x = int(input("Please enter a number: "))

x %= 100

print("The last two Digits are:","{:>02d}".format(x))