size = 20
canvas = []
line = ""
for i in range(size):
    canvas.append([" "] * size)

canvas[10][5] = "*"

print("+" + "-" * size + "+")
#y
for i in range(len(canvas)-1, 0, -1):
    #x
    for j in range(len(canvas[i])):
        line += canvas[i][j]
    print("|" + line + "|")
    line = ""

print("+" + "-" * size + "+")
