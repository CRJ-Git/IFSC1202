x = input("Please enter a string of integers separated by spaces: ")

y = x.split(' ')

for i in range(len(y)-1):
    if y[i] < y[i+1]:
        print(y[i+1])