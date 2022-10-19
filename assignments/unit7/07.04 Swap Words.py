x = input("Please enter a string with two words separated by a space: ")

firstWord = x[:x.find(" ")]

secondWord = x[x.find(" ")+1:]

print(secondWord + " " + firstWord)

