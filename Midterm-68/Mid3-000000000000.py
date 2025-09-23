# ชือ (งานนี้ 18 คะแนน)
print(">> Program Calculator Grade <<\n")
result, ts, tp, tc = "", 0, 0, 0
for i in range(6):
    name = input(f"Enter name  #{i+1} : ")
    score = int(input(f"Enter score #{i+1} : "))
    if score >= 80 and score <= 100: grade, level, point = "A", 4, 4 * 3
    elif score >= 70: grade, level, point = "B", 3, 3 * 3
    elif score >= 60: grade, level, point = "C", 2, 2 * 3
    elif score >= 50: grade, level, point = "D", 1, 1 * 3
    elif score >=  0: grade, level, point = "F", 0, 0 * 3
    tc += 3
    tp += point
    result += f"| {i+1} | {name:11}|{score:5.1f}|  {grade}  |  {level}  |   {3}  |  {point:2} |\n"
    print()
head = "|No.|Name subject|Score|Grade|Leval|Credit|Point|"
line = "=" * len(head)
print(f"{"Report Grade":^{len(head)}}")
print(line,head,line,result+line,sep="\n")
print(f"|                Total             |  {tc:2}  |  {tp:2} |",line,sep="\n")
print(f"| {f"Grade Point Average (GPA) : {tp / tc:.2f}":46}|",line,sep="\n")