classroomA = int(input("Enter Classroom A: "))
classroomB= int(input("Enter Classroom B: "))
classroomC = int(input("Enter Classroom C: "))

desksA = int((classroomA / 2)) + (classroomA % 2)
desksB = int((classroomB / 2)) + (classroomB % 2)
desksC = int((classroomC / 2)) + (classroomC % 2)
print(desksA + desksB + desksC)