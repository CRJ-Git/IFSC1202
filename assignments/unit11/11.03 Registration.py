class Student():
    def __init__(self, firstname, lastname, tnumber):
        self.firstname = firstname
        self.lastname = lastname
        self.tnumber = tnumber
        courseList = []

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
        #filename = "/workspace/IFSC1202/assignments/unit11/11.03 Students.txt"
        fin = open(filename)
        line = fin.readline()
        while line != "":
            v = line.split(",")
            v[2] = v[2].replace("\n", "")
            add_student(v[0], v[1], v[2])
            line = fin.readline()

class Course():
    def __init__(self, department, number, name, room, meetingtimes):
        self.department = department
        self.number = number
        self.name = name
        self.room = room
        self.meetingtimes = meetingtimes

class CourseList():
    def __init__(self):
        courselist = []
    
    def add_course(self, department, number, name, room, meetingtimes):
        newCourse = Course(department, number, name, room, meetingtimes)
        courselist.append(newCourse)
    
    def find_course(self, departmenttofind, numbertofind):
        for i in range(len(courselist)):
            if courselist[i].department == departmenttofind and courselist[i].number == numbertofind:
                return i
        return -1
    
    def add_course_from_file(self, filename):
        #filename ="/workspace/IFSC1202/assignments/unit11/11.03 Courses.txt"
        fin = open(filename)
        line = fin.readline()
        
        while line != "":
            v = line.split(",")
            v[4] = v[4].replace("\n", "")
            CourseList.add_course(v[0], v[1], v[2], v[3], v[4])

#start of main program:

mainCourseList = CourseList()

mainCourseList.add_course_from_file("/workspace/IFSC1202/assignments/unit11/11.03 Courses.txt")

mainStudentList = StudentList()

mainStudentList.add_student_from_file("/workspace/IFSC1202/assignments/unit11/11.03 Students.txt")

fin = open("/workspace/IFSC1202/assignments/unit11/11.03 Registration.txt")
line = fin.readline()

while line != "":
    v = line.split(",")
    v[2] = v[2].replace("\n", "")
    coursetoadd = mainCourseList.courselist[mainCourseList.find_course(v[1], v[2])]
    mainStudentList.studentvector[mainStudentList.find_student(v[0])].CourseList.append(coursetoadd)
    line = fin.readline()

mainStudentList.print_student_list()