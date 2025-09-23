# g = {80:"A",70:"B",60:"C",50:"D",0:"F"}
# num = int(input("Enter score : "))  
# if 0 < num <= 100:
#     for i in g:
#         if num >= i and num <= 100:
#             grade = g[i]
#             break
#     print("Score value ",num,", got grade ",grade,sep="")
# else: print("Score not in range.")


# num = int(input("Enter score : "))
# if num >= 80 and num <= 100: grade = "A"
# elif num >= 70 and num < 80: grade = "B"
# elif num >= 60 and num < 70: grade = "C"
# elif num >= 50 and num < 60: grade = "D"
# else: grade = "F"
# print(f"Score value {num}, got grade {grade}") if num >= 0 and num <= 100 else print("Score not in range.")


#case 1 
# score = int(input("Enter score : "))
# if score >= 0 and score <= 100: 
#     grade = ""
#     if score >= 80 and score <= 100:
#         grade = "A"
#     else:
#         if score >= 70 and score <= 79:
#             grade = "B"
#         else:
#             if score >= 60 and score <= 69:
#              grade = "C"
#             else:
#                 if score >= 50 and score <= 59:
#                     grade = "C"
#                 else:
#                     grade = "F"
#     print("Your score",score,"got grade",grade)
# else:
#     print("Score not in range")


#case2
# score = int(input("Enter score : "))
# if score >= 0 and score <= 100:
#     grade = ""
#     if score >= 80 and score <= 100:
#         grade = "A"
#     elif score >= 70 and score < 80:
#         grade = "B"
#     elif score >= 60 and score < 70:
#         grade = "C"
#     elif score >= 50 and score < 60:
#         grade = "D"
#     else: grade = "F"
#     print("Your score",score,"got grade",grade)
# else:
#     print("Score not in range")


#case3 
score = int(input("Enter score : "))
if score >= 0 and score <= 100:
    grade = ""
    match score:
        case s if 80 <= s <= 100:
            grade = "A"
        case s if 70 <= s <= 79:
            grade = "B"
        case s if 60 <= s <= 69:
            grade = "C"
        case s if 50 <= s <= 59:
            grade = "D"
        case s if 0 <= s <= 49:
            grade = "F"
    print("Your score:",score,"got grade",grade)
else: print("Score not in range")

score = int(input("Enter score : "))
if score >= 0 and score <= 100:
    grade = ""
    if score >= 80 and score <= 100: grade = "A"
    if score >= 70 and score <= 79: grade = "B"
    if score >= 60 and score <= 69: grade = "C"
    if score >= 50 and score <= 59: grade = "D"
    if score >= 0 and score <= 49: grade = "f"
    print("Your score:",score,"got grade",grade)
else: print("Score not in range")