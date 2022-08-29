hours1 = input("Please enter the hours for timestamp one: ")
minutes1 = input("Please enter the minutes for timestamp one: ")
seconds1 = input("Please enter the seconds for timestamp one: ")

hours2 = input("Please enter the hours for timestamp two: ")
minutes2 = input("Please enter the minutes for timestamp two: ")
seconds2 = input("Please enter the seconds for timestamp two: ")

hour_total = int(hours2) - int(hours1) * 60 * 60
minute_total = int(minutes2) - int(minutes1) * 60
second_total = int(seconds2) - int(seconds1)
print(hour_total + minute_total + second_total)