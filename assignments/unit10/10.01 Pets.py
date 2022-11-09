class Pet ():
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age

petfile = open("/workspace/IFSC1202/assignments/unit10/10.01 Pets.txt")

line = petfile.readline()

petArray = []

while line != "":
    #v for vector
    v = line.split(", ")
    newPet = Pet(v[0], v[1], v[2])
    petArray.append(newPet)
    line = petfile.readline()

print("{:^10}{:^10}{:^10}" .format("Name", "Type", "Age"))

for i in range(len(petArray)):
    print("{:^10}{:^10}{:^10}" .format(petArray[i].name, petArray[i].type, petArray[i].age))