from math import pi

class ball():
    def __init__(self, balltype = "Basketball", diameter = 9.51, pressure = 8.0):
        self.balltype = balltype
        self.diameter = diameter
        self.pressure = pressure

def Circumference(self):
    circumference = math.pi * self.diameter
    return circumference

def ChangePressure(self, pressurechange):
    self.pressure += pressurechange
    return self.pressure

myball1 = Ball("Basketball", 9.51, 8.0)
myball2 = Ball("Volleyball", 8.15, 7.5)
myball3 = Ball("Soccerball", 8.65, 9.0)
myball4 = Ball()

