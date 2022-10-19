x = input("Please enter a string containing integers separated by spaces: ")

y = x.split(' ')

for i in range(1, len(y), 2):
    print(y[i])
