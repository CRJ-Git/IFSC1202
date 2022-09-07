x = int(input("Please enter a two digit number: "))

tens = x // 10

ones = x % 10

print("Tens digit:""{:^5d}".format(tens))
print("Ones digit:""{:^5d}".format(ones))