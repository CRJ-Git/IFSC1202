babyNamesFile = open("/workspace/IFSC1202/assignments/Exam Two Names.txt")

namesLine = babyNamesFile.readline()

boysNames = []

girlsNames = []

userInput = ''

while namesLine != '':
    x = namesLine.split(',')
    
    boysNames.append(x[0])

    x[1] =  x[1].strip()

    x[1] = x[1].replace('\n','')

    girlsNames.append(x[1])

    namesLine = babyNamesFile.readline()


while userInput != 'Q' or 'q':
    #userInput = input("Please enter a name (or Q to exit): ")
    userInput = "Liam"

    userInput = userInput.strip()

    userInput = userInput.capitalize()

    for i in range(len(boysNames)):
        if userInput == boysNames[i]:
            print("{} - Rank {}".format(boysNames[i], i))
