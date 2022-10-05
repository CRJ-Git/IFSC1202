from math import pi

def diameter(radius):
    d = radius * 2
    return d

def circumference(radius):
    c = 2 * pi * radius
    return c

def area(radius):
    a = pi * radius ** 2
    return a

radiusfile = open("/workspace/IFSC1202/assignments/unit6/06.01 Radius.txt")

radius = radiusfile.readline()

print("{:^15s}".format("Radius", "Diameter", "Circumference", "Area"))

while radius != "":
    d = float(diameter(radius))
    c = float(circumference(radius))
    a = float(area(radius))

