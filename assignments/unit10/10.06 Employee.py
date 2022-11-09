class Employee ():
    def __init__(self, firstname, lastname, id, hours, wage):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.hours = hours
        self.wage = wage
    
    def WeeklyPay(self, wage, hours):
        if int(hours) <= 40:
            return float(wage) * int(hours)
        if int(hours) > 40:
            return (float(wage) * 40) + (1.5 * float(wage) * (int(hours) - 40))

roster = []

payrollfile = open("/workspace/IFSC1202/assignments/unit10/10.06 Payroll.txt")

line = payrollfile.readline()

while line != "":
     #v for vector
    v = line.split(", ")
    v[4] = v[4].replace("\n", "")
    roster.append(Employee(v[0], v[1], v[2], v[3], v[4]))

    line = payrollfile.readline()

print("{:^12}{:^12}{:^12}{:^12}{:^12}{:^12}" .format("First Name", "Last Name", "ID", "Hours", "Wage", "Weekly Pay"))

for i in range(len(roster)):
    print("{:^12}{:^12}{:^12}{:^12}{:^12.2f}{:^12.2f}" .format(roster[i].firstname, roster[i].lastname, roster[i].id, roster[i].hours, float(roster[i].wage), roster[i].WeeklyPay(roster[i].wage, roster[i].hours)))