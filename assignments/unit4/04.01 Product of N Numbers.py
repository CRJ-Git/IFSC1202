n = int(input("Please enter the number of integers to multiply: "))

result = 1

for i in range(1, n + 1):
    result *= int(input("Enter Number: "))

print(result)