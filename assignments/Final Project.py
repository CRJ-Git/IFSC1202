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
        

    def penup():
        pen = "U"
    
    def pendown():
        pen = "D"
    
    def turnleft():
        if direction == "U":
            direction = "L"
        if direction == "L":
            direction = "D"
        if direction == "D":
            direction = "R"
        if direction == "R":
            direction = "U"
    
    def turnright():
        if direction == "U":
            direction = "R"
        if direction == "R":
            direction = "D"
        if direction == "D":
            direction = "L"
        if direction == "L":
            direction = "U"
    
    def move(self, distance):
        
        