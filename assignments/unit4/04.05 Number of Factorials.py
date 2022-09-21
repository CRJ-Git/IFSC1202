n = int(input("Please enter an integer for N: "))

result = 0
x = 1

for i in range(1, n + 1):
    x *= i
    result += x

print("Sum of Factorials: ", result)