popFile = open("/workspace/IFSC1202/assignments/unit8/08.11 USPopulation.txt")

x = popFile.readline()

popList = []

while x != "":
    popList.append(int(x))
  
    x = popFile.readline()

for i in range(0,len(popList)-1):
    popList[i] *= 1000

year = 1950

change = 0

pChange = 0.0

print("{:^6}{:^12}{:^8}{:^16}".format("Year","Population","Change","Percent Change"))

print("{:^6}{:^12}{:^8}{:^16}".format(year,popList[0],change,pChange))

for i in range(1,len(popList)-1):
    year += 1

    change = popList[i] - popList[i-1]

    pChange = (change / popList[i-1]) * 100

    print("{:^6}{:^12}{:^8}{:^16.2}".format(year,popList[i],change,pChange))