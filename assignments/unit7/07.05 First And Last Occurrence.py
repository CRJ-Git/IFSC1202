x = input("Please enter a string: ")

letterIndex = x.find("f")

lastIndex = x.rfind("f")

if letterIndex > -1:
    print("first occurrence: " + str(letterIndex))

if lastIndex != letterIndex:
    print("last occurrence: " + str(lastIndex))

