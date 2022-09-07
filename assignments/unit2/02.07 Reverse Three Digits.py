usernumber = int(input("Please enter a three digit number: "))

ones = usernumber // 100
tens = (usernumber // 10) % 10
hundreds = usernumber % 10

print("Reverse of Digits: ","{:1d}".format(hundreds) + "{:1d}".format(tens) + "{:1d}".format(ones))