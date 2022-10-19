x = input("Please enter a string of integers separated by spaces: ")

y = x.split(' ')

for i in range(len(y)-1):
    if int(y[i]) < 0 and int(y[i+1]) < 0:
        print (y[i] + ' ' + y[i+1])
    if int(y[i]) > 0 and int(y[i+1]) > 0:
        print (y[i] + ' ' + y[i+1])