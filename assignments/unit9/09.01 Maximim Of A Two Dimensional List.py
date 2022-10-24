x =  "3 4" #input("Enter two integers for row and column: ")

y = x.split(" ")

m = int(y[0])
n = int(y[1])

dataArray = []

for i in range(m):
    dataInput = "1 2 3 4" #input("Please enter a line of data: ")
    dataLine = dataInput.split(" ")
    dataArray.append(dataLine)

for i in range(m):
    for j in range(n):
        print(dataArray[i][j], end=' ')
    print('\n')

