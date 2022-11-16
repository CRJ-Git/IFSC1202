class Student():
    def __init__(self, firstname, lastname, tnumber):
        self.firstname = firstname
        self.lastname = lastname
        self.tnumber = tnumber
        courselist = []

class StudentList():
    def __init__(self):
        studentvector = []
    
    def add_student(self, firstname, lastname, tnumber):
        newStudent = Student(firstname, lastname, tnumber)
        studentvector.append(newStudent)
    
    def find_student(self, studenttofind):
        for i in range(len(studentvector)):
            if studentvector[i].tnumber == studenttofind:
                return i
        return -1

    def print_student_list(self):
        print("{:<14}{:<14}{:<14}{:<15}{:<50}{:<14}{:<15}".format("First Name", "Last Name", "T-Number", "Course", "Name", "Room", "Meeting Times"))
        for i in range(len(studentvector)):
            print("{:<14}{:<14}{:<14}".format(studentvector[i].firstname, studentvector[i].lastname, studentvector[i].tnumber))
            for j in range(len(studentvector[i].courselist)):
                print("{:<15}{:<50}{:<14}{:<15}".format(studentvector[i].courselist[j].department + " " + studentvector[i].courselist[j].number, studentvector[i].courselist[j].name, studentvector[i].courselist[j].room, studentvector[i].courselist[j].meetingtimes))
    
    def add_student_from_file(self, filename):
        fin = open("/workspace/IFSC1202/assignments/unit11/11.03 Students.txt")