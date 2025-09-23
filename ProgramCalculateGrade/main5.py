print("Program Calculate Grade\n\nInput Data: ")
result,t_c,t_p = "",0,0
for i in range(1,7):
    score = float(input(f"Enter score of subject  #{i} : "))
    credit = int(input(f"Enter credit of subject #{i} : "))
    if score >= 80: grade,point = "A",credit * 4
    elif score >= 70: grade,point = "B",credit * 3
    elif score >= 60: grade,point = "C",credit * 2
    elif score >= 50: grade,point = "D",credit * 1
    else: grade,point = "F",credit * 0
    result += f"| {i} |  {score:4.1f} |  {grade}  |   {credit}  |  {point:4.1f} |\n"
    t_c += credit
    t_p += point
head = "|No.|  Mark  Grade|Credit| Points|"
line = "=" * len(head)
result += line
print(f"\n{"Report Grade":^{len(head)}}",line,head,line,result,sep="\n")
print(f"|       Total     | {int(t_c):.1f} |  {int(t_p):.1f} |",line,sep="\n")
print(f"Grade Point Average(GPA) : {t_p / t_c:.2f}")


# print("Program Calculate Grade\n\nInput Data:")
# result,t_c,t_p = "",0 ,0
# for i in range(1,7):
#     score = float(input(f"Enter score of subject  #{i} : "))
#     credit = int(input(f"Enter credit of subject #{i} : "))
#     if score >= 80 and score <= 100:
#         grade = "A"
#         point = credit * 4
#     elif score >= 70:
#         grade  = "B"
#         point = credit * 3
#     elif score >= 60:
#         grade = "C"
#         point = credit * 2
#     elif score >= 50:
#         grade = "D"
#         point = credit * 1
#     else:
#         grade = "F"
#         point = credit * 0
#
#     t_c += credit
#     t_p += point
#
#     result += f"| {i} |  {score:4} |  {grade}  |   {credit}  |  {point:>4.1f} |\n"
#
#
# head = "|No.|  Mark |Grade|Credit| Points|"
# line = "=" * len(head)
# result += line
# print(f"\n{"Report Grade":^{len(head)}}")
# print(line,head,line,sep="\n")
# print(result)
# print(f"        Total     | {t_c:.1f} |  {t_p:.1f} |")
# print(line)
# print(f"Grade Point Average(GPA) : {t_p / t_c:.2f}")


