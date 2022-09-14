x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x == y and x == z:
    print(3)
elif x == y or x == z or y == z:
    print(2)
else:
    print(0)