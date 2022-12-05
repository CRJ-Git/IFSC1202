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
        for i in range(len(self.canvas)-1, 0, -1):
            #x
            for j in range(len(self.canvas[i])):
                line += self.canvas[i][j]
            print("|" + line + "|")
            line = ""
        
        print("+" + "-" * size + "+")
        print("X = " + str(self.xpos) + " Y = " + str(self.ypos) + " Direction = " + str(self.direction))
    
    def penup(self):
        self.pen = "U"
    
    def pendown(self):
        self.pen = "D"
    
    def turnleft(self):
        #no switch! :(  looking it up I think I could use match/case,
        #but I think for this use case if/elif statements will work
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
        
        if self.direction == "U":
            for i in range(distance):
                if self.pen == "D":
                    self.canvas[self.ypos][self.xpos] = "*"
                self.ypos += 1
                if self.ypos > size-1:
                    self.ypos = size-1

        elif self.direction == "R":
            for i in range(distance):
                if self.pen == "D":
                    self.canvas[self.ypos][self.xpos] = "*"
                self.xpos += 1
                if self.xpos > size-1:
                    self.xpos = size-1
        
        elif self.direction == "D":
            for i in range(distance):
                if self.pen == "D":
                    self.canvas[self.ypos][self.xpos] = "*"
                self.ypos -= 1
                if self.ypos < 0:
                    self.ypos = 0
        
        elif self.direction == "L":
            for i in range(distance):
                if self.pen == "D":
                    self.canvas[self.ypos][self.xpos] = "*"
                self.xpos -= 1
                if self.xpos < 0:
                    self.xpos = 0

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
    command = command.split(",")
    #here I implement the command structure (probably better to implement it elsewhere but I think this is fine)
    if int(command[0]) == 1:
        turtlegraphics.penup()
    elif int(command[0]) == 2:
        turtlegraphics.pendown()
    elif int(command[0]) == 3:
        turtlegraphics.turnright()
    elif int(command[0]) == 4:
        turtlegraphics.turnleft()
    elif int(command[0]) == 5:
        turtlegraphics.move(int(command[1]))
    elif int(command[0]) == 6:
        turtlegraphics.printsketch()
    cshapeline = cshapefile.readline()