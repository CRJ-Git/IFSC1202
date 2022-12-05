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
    
    def printsketch():
        #here I decided to use a string variable to print the canvas
        line = ""
        print("+" + "-" * size + "+")
        #y
        for i in range(len(canvas)):
            #x
            for j in range(len(canvas[i])):
                line += canvas[i][j]
            print("|" + line + "|")
            line = ""
        
        print("+" + "-" * size + "+")
        print("X = " + self.xpos + " Y = " + self.ypos + " Direction = " + self.direction)
    
    def penup():
        self.pen = "U"
    
    def pendown():
        self.pen = "D"
    
    def turnleft():
        #no switch! :(  looking it up I think I could use match/case but I think for this use case, if statements will work
        if self.direction == "U":
            self.direction = "L"
        elif self.direction == "L":
            self.direction = "D"
        elif self.direction == "D":
            self.direction = "R"
        elif self.direction == "R":
            self.direction = "U"
    
    def turnright():
        if self.direction == "U":
            self.direction = "R"
        elif self.direction == "R":
            self.direction = "D"
        elif self.direction == "D":
            self.direction = "L"
        elif self.direction == "L":
            self.direction = "U"
    
    def move(self, distance):
        #here is where the hint would probably apply, as the y position values have to work in reverse
        if direction == "U":
            for i in range(distance):
                if pen == "D":
                    canvas[ypos][xpos] = "*"
                ypos -= 1
                if ypos < 0:
                    ypos = 0

        elif self.direction == "R":
            xpos += distance
        elif self.direction == "D":
            ypos += distance
        elif self.direction == "L":
            xpos -= distance
            