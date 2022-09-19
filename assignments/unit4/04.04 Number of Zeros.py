n = int(input("Please enter an integer for N: "))

zeroes = 0

for i in range(1, n+1):
    x = int(input("Enter Number: "))
    if x == 0:
        zeroes += 1

print(zeroes)