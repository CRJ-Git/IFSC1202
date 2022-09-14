x = int(input("Please enter a 3 digit number: "))
 
ones = x % 10
tens = (x // 10) % 10
hundreds = x // 100

if ones > tens and tens > hundreds:
    print("YES")
else:
    print("NO")