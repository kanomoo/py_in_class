# def check_Point(grade):
#     point = 0
#     if grade == "A": point = 4
#     elif grade == "B": point = 3
#     elif grade == "C": point = 2
#     elif grade == "D": point = 1
#     elif grade == "F": point = 0
#     return point

# Done = True
# while Done:
#     grade = input("Enter grade (Q-exit): ").upper()
#     grade = grade.upper()
#     if grade == "Q": Done = False
#     else:
#         value = check_Point(grade)
#         print(f"Point value of {grade} is {value}")
# print("End Program.")

# def Check_point(grade):
#     grades = ("A","B","C","D","F")
#     values = (4,3,2,1,0)
#     for i in range(len(grades)):
#         if grade == grades[i]: return values[i]

# while True:
#     grade = input("Enter grade (Q-exit): ").upper()
#     point = Check_point(grade)
#     if grade != "Q": print(f"Point value of {grade} is {point}")
#     else: break
# print("End Program.")


def Check_grade(grade: str):
    check = {"A":4,"B":3,"C":2,"D":1,"F":0}
    if grade in check: return check[grade]

while True:
    grade = input("Enter grade (Q-exit): ").upper()
    point = Check_grade(grade)
    if grade != "Q": print(f"Point value of {grade} is {point}")
    else: break
print("End Program.")