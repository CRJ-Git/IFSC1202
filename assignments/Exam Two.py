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

userInput = input("Please enter a name (or Q to exit): ")
userInput = userInput.strip()
userInput = userInput.capitalize()
while userInput != 'Q':
  
    userInput = userInput.strip()

    userInput = userInput.capitalize()

    for i in range(0,len(boysNames)):
        if userInput == boysNames[i]:
            print("{} - Rank {}".format(boysNames[i], i+1))
               
        elif userInput == girlsNames[i]:
            print("{} - Rank {}".format(girlsNames[i], i+1))

        elif i == len(boysNames)-1:
            print("Name Not Found")
    
    userInput = input("Please enter a name (or Q to exit): ")
    userInput = userInput.strip()
    userInput = userInput.capitalize()
            
            
        
            
    
