print("Program Calculater Grade\n")
print("Input Data:")
score_subject1 = float(input("Enter score of subject  #1: "))
credit_subject1 = int(input("Enter credit of subject #1: "))
score_subject2 = float(input("Enter score of subject  #2: "))
credit_subject2 = int(input("Enter credit of subject #2: "))
score_subject3 = float(input("Enter score of subject  #3: "))
credit_subject3 = int(input("Enter credit of subject #3: "))
score_subject4 = float(input("Enter score of subject  #4: "))
credit_subject4 = int(input("Enter credit of subject #4: "))
score_subject5 = float(input("Enter score of subject  #5: "))
credit_subject5 = int(input("Enter credit of subject #5: "))
score_subject6 = float(input("Enter score of subject  #6: "))
credit_subject6 = int(input("Enter credit of subject #6: "))


if(score_subject1 >= 80):
    grade1 = "A"
    point1 = 4 * credit_subject1
    grade_int1 = 4
elif(score_subject1 >= 70):    
    grade1 = "B"
    point1 = 3 * credit_subject1
    grade_int1 = 3
elif(score_subject1 >= 60):
    grade1 = "C"
    point1 = 2 * credit_subject1
    grade_int1 = 2
elif(score_subject1 >= 50):
    grade1 = "D"
    point1 = 1 * credit_subject1
    grade_int1 = 1

if(score_subject2 >= 80):
    grade2 = "A"
    point2 = 4 * credit_subject2
    grade_int2 = 4
elif(score_subject2 >= 70):    
    grade2 = "B"
    point2 = 3 * credit_subject2
    grade_int2 = 3
elif(score_subject2 >= 60):
    grade2 = "C"
    point2 = 2 * credit_subject2
    grade_int2 = 2
elif(score_subject2 >= 50):
    grade2 = "D"
    point2 = 1 * credit_subject2
    grade_int2 = 1

if(score_subject3 >= 80):
    grade3 = "A"
    point3 = 4 * credit_subject3
    grade_int3 = 4
elif(score_subject3 >= 70):
    grade3 = "B"
    point3 = 3 * credit_subject3
    grade_int3 = 3
elif(score_subject3 >= 60):
    grade3 = "C"
    point3 = 2 * credit_subject3
    grade_int3 = 2
elif(score_subject3 >= 50):
    grade3 = "D"
    point3 = 1 * credit_subject3
    grade_int3 = 1

if(score_subject4 >= 80):
    grade4 = "A"
    point4 = 4 * credit_subject4
    grade_int4 = 4
elif(score_subject4 >= 70):
    grade4 = "B"
    point4 = 3 * credit_subject4
    grade_int4 = 3
elif(score_subject4 >= 60):
    grade4 = "C"
    point4 = 2 * credit_subject4
    grade_int4 = 2
elif(score_subject4 >= 50):
    grade4 = "D"
    point4 = 1 * credit_subject4
    grade_int4 = 1

if(score_subject5 >= 80):
    grade5 = "A"
    point5 = 4 * credit_subject5
    grade_int5 = 4
elif(score_subject5 >= 70):
    grade5 = "B"
    point5 = 3 * credit_subject5
    grade_int5 = 3
elif(score_subject5 >= 60):
    grade5 = "C"
    point5 = 2 * credit_subject5
    grade_int5 = 2
elif(score_subject5 >= 50):
    grade5 = "D"
    point5 = 1 * credit_subject5
    grade_int5 = 1

if(score_subject6 >= 80):
    grade6 = "A"
    point6 = 4 * credit_subject6
    grade_int6 = 4
elif(score_subject6 >= 70):
    grade6 = "B"
    point6 = 3 * credit_subject6
    grade_int6 = 3
elif(score_subject6 >= 60):
    grade6 = "C"
    point6 = 2 * credit_subject6
    grade_int6 = 2
elif(score_subject6 >= 50):
    grade6 = "D"
    point6 = 1 * credit_subject6
    grade_int6 = 1

# noinspection PyUnboundLocalVariable
point1 = float(point1)
point2 = float(point2)
point3 = float(point3)
point4 = float(point4)
point5 = float(point5)
point6 = float(point6)


total_credit = credit_subject1 + credit_subject2 + credit_subject3 + credit_subject4 + credit_subject5 + credit_subject6
total_point = point1 + point2 + point3 + point4 + point5 + point6
gpa = round(total_point / total_credit,2)

print("\n           Report Grade            ")
print("===================================")
print("|No.|  Mark  |Grade|Credit| Points|")
print("===================================")
print("| 1 |  ", score_subject1, "| ",grade1, " |  ", credit_subject1, " |  ",point1,"|")
print("| 2 |  ", score_subject2, "| ",grade2, " |  ", credit_subject2, " |  ",point2,"|")
print("| 3 |  ", score_subject3, "| ",grade3, " |  ", credit_subject3, " |  ",point3,"|")
print("| 4 |  ", score_subject4, "| ",grade4, " |  ", credit_subject4, " |  ",point4,"|")
print("| 5 |  ", score_subject5, "| ",grade5, " |  ", credit_subject5, " | ",point5,"|")
print("| 6 |  ", score_subject6, "| ",grade6, " |  ", credit_subject6, " |  ",point6,"|")
print("===================================")
print("|        Total     | ",total_credit," | ",point1 + point2 + point3 + point4 + point5 + point6,"|")
print("===================================")
print("Grade Point Average(GPA) : ",(gpa))