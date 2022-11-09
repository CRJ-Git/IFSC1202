class RetailItem ():
    def __init__(self, description = "", unitsonhand = 0, price = 0.0):
        self.description = description
        self.unitsonhand = unitsonhand
        self.price = price
    
    def InventoryValue(unitsonhand, price):
        value = unitsonhand * price
        return value

itemVector = []

inventoryfile = open("/workspace/IFSC1202/assignments/unit10/10.02 Inventory.txt")

inventoryline = inventoryfile.readline()

while inventoryline != "":
    v = inventoryline.split("")