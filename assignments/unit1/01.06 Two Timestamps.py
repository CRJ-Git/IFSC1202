print("First Timestamp:")
hours1 = int(input("Please enter the hours for timestamp one: "))
minutes1 = int(input("Please enter the minutes for timestamp one: "))
seconds1 = int(input("Please enter the seconds for timestamp one: "))

print("Second Timestamp:")
hours2 = int(input("Please enter the hours for timestamp two: "))
minutes2 = int(input("Please enter the minutes for timestamp two: "))
seconds2 = int(input("Please enter the seconds for timestamp two: "))

total1 = (hours1 * 60 * 60) + (minutes1 * 60) + seconds1
total2 = (hours2 * 60 * 60) + (minutes2 * 60) + seconds2

print(total2 - total1)