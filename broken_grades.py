# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) #added int(

exam_three = int(input("Input exam grade three: ")) #change 3 to three for concistency, change string data type to integer data type

grades = [exam_one,exam_two, exam_three] # added commas between each element in the list
sum = 0
for grade in grades: #change right hand side grade to grades 
  sum = sum + grade

avg = sum / len(grades) #spelling error grdes corrected to grades

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: #added a full colon at the end
    letter_grade = "B"
elif avg >= 70 and avg < 80: #eddited numbers to fit marking criteria 69 changed to 70 
    letter_grade = "C" # change "c' to "c" 
elif avg >= 60 and avg <= 69: # edited <=69 to >=60 and >=65 to <=69 to meet marking criteria 
    letter_grade = "D"
else: # elif statement changed to else
    letter_grade = "F"

#for grade in grades: remove this line as it makes it print three times and then reindent the print statement
print("Exam: " + str(grade))
print("Average: " + str(avg))
print("Grade: " + letter_grade)

if letter_grade == "F": #letter-grade hyphen changed to underscore and the is operator checks if two variables refer to the same object, but == checks if their values are equal.
    print ("Student is failing.") #added brackets for print statement
else:
    print ("Student is passing.") #added brackets for print statement
