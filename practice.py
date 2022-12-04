size = 20
canvas = []
line = ""
for i in range(size):
    canvas.append([" "] * size)

canvas[1][10] = "*"

print("+" + "-" * size + "+")
#y
for i in range(len(canvas)):
    #x
    for j in range(len(canvas[i])):
        line += canvas[i][j]
    print("|" + line + "|")
    line = ""

print("+" + "-" * size + "+")
