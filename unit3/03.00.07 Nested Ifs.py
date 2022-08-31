x = int(input("Enter x:  "))
y = int(input("Enter y:  "))
if x > 0:
    if y > 0:
        # x > 0, y > 0
        print("Quadrant I")
    else:
        # x > 0, y <= 0
        print("Quadrant IV")
else:
    if y > 0:
        # x <= 0, y > 0
        print("Quadrant II")
    else:
        # x <= 0, y <= 0
        print("Quadrant III")
