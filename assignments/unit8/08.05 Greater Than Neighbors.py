x = input("Please enter a string of integers separated by spaces: ")

y = x.split(' ')

z = 0

for i in range(1,len(y)-1):
    if int(y[i-1]) < int(y[i]) > int(y[i+1]):
        z += 1

print(z)