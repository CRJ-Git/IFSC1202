x = input("Please enter a string of integers sesparated by spaces: ")

y = x.split(' ')

for i in range(len(y)):
    if i%2 != 1:
        print(y[i])