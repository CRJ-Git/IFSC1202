print("Please enter 3 numbers, with two of them equal to each other.")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x == y:
    print(3)
elif x == z:
    print(2)
else:
    print(1)