class Sketch ():
    def __init__(self, size):
        self.size = size
        self.xpos = 0
        self.ypos = 0
        self.direction = "U"
        self.pen = "U"
        self.canvas = []
        for i in range(size):
            self.canvas.append([" "] * size)
    
    def printsketch(self):
        #here I decided to use a string variable to print the canvas
        line = ""
        print("+" + "-" * size + "+")
        #y
        for i in range(len(canvas)-1, 0, -1):
            #x
            for j in range(len(canvas[i])):
                line += canvas[i][j]
            print("|" + line + "|")
            line = ""
        
        print("+" + "-" * size + "+")
        print("X = " + self.xpos + " Y = " + self.ypos + " Direction = " + self.direction)
    
    def penup(self):
        self.pen = "U"
    
    def pendown(self):
        self.pen = "D"
    
    def turnleft(self):
        #no switch! :(  looking it up I think I could use match/case but I think for this use case, if statements will work
        if self.direction == "U":
            self.direction = "L"
        elif self.direction == "L":
            self.direction = "D"
        elif self.direction == "D":
            self.direction = "R"
        elif self.direction == "R":
            self.direction = "U"
    
    def turnright(self):
        if self.direction == "U":
            self.direction = "R"
        elif self.direction == "R":
            self.direction = "D"
        elif self.direction == "D":
            self.direction = "L"
        elif self.direction == "L":
            self.direction = "U"
    
    def move(self, distance):
        
        if direction == "U":
            for i in range(distance):
                while pen == "D":
                    canvas[ypos][xpos] = "*"
                ypos += 1
                if ypos > size-1:
                    ypos = size-1

        elif self.direction == "R":
            for i in range(distance):
                while pen == "D":
                    canvas[ypos][xpos] = "*"
                xpos += 1
                if xpos > size-1:
                    xpos = size-1
        
        elif self.direction == "D":
            for i in range(distance):
                while pen == "D":
                    canvas[ypos][xpos] = "*"
                ypos -= 1
                if ypos < 0:
                    ypos = 0
        
        elif self.direction == "L":
            for i in range(distance):
                while pen == "D":
                    canvas[ypos][xpos] = "*"
                xpos += 1
                if xpos < 0:
                    xpos = 0

#getting the file
cshapefile = open("/workspace/IFSC1202/assignments/Cshape.txt")

#here I just grab the first line to indicate size
size = cshapefile.readline()

size = int(size.replace("\n", ""))

#creating new object
turtlegraphics = Sketch(size)

#grabbing all the commands and drawing the shape
cshapeline = cshapefile.readline()
while cshapeline != "":
    command = cshapeline.replace("\n", "")
    command = cshapeline.split(",")
    #here I implement the command structure (probably better to implement it elsewhere but I think this is fine)
    if command[0] == 1:
        turtlegraphics.penup()
    elif command[0] == 2:
        turtlegraphics.pendown()
    elif command[0] == 3:
        turtlegraphics.turnright()
    elif command[0] == 4:
        turtlegraphics.turnleft()
    elif command[0] == 5:
        turtlegraphics.move(command[1])
    elif command[0] == 6:
        turtlegraphics.printsketch()
    cshapeline = cshapefile.readline()