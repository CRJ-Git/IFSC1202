a = int(input("Enter first coordinate: "))
b = int(input("Enter second coordinate: "))
c = int(input("Enter third coordinate: "))

atob = a - b
atoc = a - c

if atob < 0:
    atob = -atob

if atoc < 0:
    atoc = -atoc

if atob < atoc:
    print(atob)
else:
    print(atoc)