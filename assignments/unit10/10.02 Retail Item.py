class RetailItem ():
    def __init__(self, description = "", unitsonhand = 0, price = 0.0):
        self.description = description
        self.unitsonhand = unitsonhand
        self.price = price
    
    def InventoryValue(self, unitsonhand, price):
        temp = int(unitsonhand) * float(price)
        return temp

itemVector = []

inventoryfile = open("/workspace/IFSC1202/assignments/unit10/10.02 Inventory.txt")

inventoryline = inventoryfile.readline()

while inventoryline != "":
    #v for vector
    v = inventoryline.split(", ")
    v[2] = v[2].replace("\n", "")
    itemVector.append(RetailItem(v[0], v[1], v[2]))
    
    inventoryline = inventoryfile.readline()

print("{:^15}{:^15}{:^15}{:^15}" .format("Description", "Units on Hand", "Price", "Inventory Value"))

for i in range(len(itemVector)):
    print("{:^15}{:^15}{:^15}{:^15.2f}" .format(itemVector[i].description, itemVector[i].unitsonhand, itemVector[i].price, itemVector[i].InventoryValue(itemVector[i].unitsonhand, itemVector[i].price)))

