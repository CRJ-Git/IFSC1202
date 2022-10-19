popFile = open("/workspace/IFSC1202/assignments/unit8/08.11 USPopulation.txt")

x = popFile.readline()

popList = []

while x != "":
    popList.append(int(x))

for i in range(0,len(popList)-1):
    popList[i] *= 1000

print(popList[0])