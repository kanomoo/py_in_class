head = ": Porgram Cal Grade :"
line, reuslt, total, Max, Min  = len(head) * "=", "", 0, 0, 0
print(line,head,line,sep="\n")
for i in range(5):
    score = int(input(f"Enter score #{i+1} : "))
    while score < 0 or score > 100:
        print("Prease input number range(0-100)")
        score = int(input(f"Enter score #{i+1} : "))
    if score >= 80 and score <= 100: grade = "A"
    elif score >= 70 and score < 80: grade = "B"
    elif score >= 60 and score < 70: grade = "C"
    elif score >= 50 and score < 60: grade = "D"
    elif score >=  0 and score < 50: grade = "F"    
    total += score
    if i == 0 : Min = score
    if score > Max : Max = score
    if score < Min : Min = score
    reuslt += f"|  {i+1}  |  {score:3}  |   {grade}   |\n"
h = "| No. | Score | Grade |"
l = f"+{(len(h)-2) * "="}+"
print("\n    Report Grade",l,h,l,reuslt+l,sep="\n")
print(f"|Average Score| {total/5:5.2f} |\n|Maximum Score| {Max:5} |\n|Maximum Score| {Min:5} |",l,sep="\n")

# score, result, total, Max, Min = 0, "", 0, 0, 0
# head = ": Program Cal Grade :"
# line = len(head) * "="
# print(line,head,line,sep="\n")
# for n in range(5):
#     score = int(input(f"Enter score #{n+1} : "))
#     if score >= 80: grade = "A"
#     elif score >= 70: grade = "B"
#     elif score >= 60: grade = "C"
#     elif score >= 50: grade = "D"
#     else: grade = "F"
#     total += score
#     if n == 0 : Min = Max = score
#     else: 
#         Max = max(Max,score)
#         Min = min(Min,score)
#     result += "|  " + str(n+1) + "  |  " + format(score,"3") + "  |   " + str(grade) + "   |\n"
# print("\n    Report Grade")
# h = "| No. | Score | Grade |"
# l = f"+{(len(h)-2) * "="}+"
# print(l,h,l,result+l,sep="\n")
# print("|Average score|", format(total/5,"4.2f"), "|")
# print("|Maximum score|", format(Max,"5"), "|")
# print("|Minimum score|", format(Min,"5"), "|")
# print(l)