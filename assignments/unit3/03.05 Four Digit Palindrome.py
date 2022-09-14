x = int(input("Please enter a 4 digit number: "))

ones = x % 10
tens = (x // 10) % 10
hundreds = (x // 100) % 10
thousands = (x // 1000)

if thousands == ones and hundreds == tens:
    print("YES")
else:
    print("NO")