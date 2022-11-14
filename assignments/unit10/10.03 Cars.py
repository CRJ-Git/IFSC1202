class Car ():
    def __init__(self, year, make, speed):
        self.year = year
        self.make = make
        self.speed = 0

    def Accelerate(self, value):
        self.speed += value
    
    def Brake(self, value):
        if int(self.speed) >= 0:
            self.speed -= value
        if int(self.speed) < 0:
            self.speed = 0

carfile = open("/workspace/IFSC1202/assignments/unit10/10.03 Cars.txt")

line = carfile.readline()

v = line.split(", ")
v[1].replace("\n", "")

car1 = Car(v[0], v[1], 0)

line = carfile.readline()

print ("Make: " + car1.make)
print ("Year: " + car1.year)
print ("{:^6}{:^6}" .format("Change", "Speed"))

while line != "":
     line.replace("\n", "")
     if int(line) >= 0:
        car1.speed = car1.Accelerate(int(line))
     if int(line) < 0:
        car1.speed = car1.Brake(int(line))
     print("{:^6}{:^6}" .format(str(line), str(car1.speed)))
     line = carfile.readline()


