usernumber = int(input("Please enter a 3 digit number: "))

result = (usernumber % 10) + (((usernumber // 10) % 10)) + (usernumber // 100)

print("Sum of Digits:","{:^4d}".format(result))