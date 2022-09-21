a = int(input("Please enter an integer for A: "))
b = int(input("Please enter an integer for B: "))

for i in range(a, b + 1):
    print(str(i) + "*" + str(i) + "=" + str(i*i))