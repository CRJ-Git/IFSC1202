x = input("Please enter a string: ")

strHalf = int(len(x)/2)

halfTwo = x[-strHalf:]

halfOne = x[:-len(halfTwo)]

print(halfTwo + halfOne)