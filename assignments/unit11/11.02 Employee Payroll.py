class Employee ():
    def __init__(self, firstname, lastname, id, hours, wage):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.hours = 0
        self.wage = wage
    
    def WeeklyPay(self, wage, hours):
        if int(hours) <= 40:
            return float(wage) * int(hours)
        if int(hours) > 40:
            return (float(wage) * 40) + (1.5 * float(wage) * (int(hours) - 40))

roster = []

def find_employee(roster, idtofind):
    for i in range(len(roster)):
        if roster[i].id == idtofind:
            return i
    return -1

payrollfile = open("/workspace/IFSC1202/assignments/unit11/11.02 Employees.txt")

line = payrollfile.readline()

while line != "":
     #v for vector
    v = line.split(", ")
    v[3] = v[3].replace("\n", "")
    roster.append(Employee(v[0], v[1], v[2], 0 , v[3]))

    line = payrollfile.readline()

updatefile = open("/workspace/IFSC1202/assignments/unit11/11.02 Hours.txt")

line = updatefile.readline()

while line != "":
    v = line.split(", ")
    v[1] = v[1].replace("\n", "")
    roster[find_employee(roster, v[0])].hours = v[1]
    line = updatefile.readline()

print("{:^12}{:^12}{:^12}{:^12}{:^12}{:^12}" .format("First Name", "Last Name", "ID", "Hours", "Wage", "Weekly Pay"))

for i in range(len(roster)):
    print("{:^12}{:^12}{:^12}{:^12}{:^12.2f}{:^12.2f}" .format(roster[i].firstname, roster[i].lastname, roster[i].id, roster[i].hours, float(roster[i].wage), roster[i].WeeklyPay(roster[i].wage, roster[i].hours)))