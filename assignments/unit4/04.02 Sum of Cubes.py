n = int(input("Please enter the number of integers: "))

result = 0

for i in range(1, n+1):
    result += i**3

print(result)