result, tc, tp = "", 0, 0
print("Input Data:")
for i in range(5):
    name = input(f"Enter subject name({i+1}) : ")
    score = float(input(f"Enter subject score({i+1}) : "))
    print()
    if score >= 80 and score <= 100: grade, point = "A", 4 * 3
    elif score >= 70 and score < 80: grade, point = "B", 3 * 3
    elif score >= 60 and score < 70: grade, point = "C", 2 * 3
    elif score >= 50 and score < 60: grade, point = "D", 1 * 3
    elif score >=  0 and score < 50: grade, point = "F", 0 * 3
    tc += 3
    tp += point
    result += f"{i+1}   {name:{len("ubject Name         Ma")}}{score:2}     {grade}      {point:.1f}\n"
head = "no. Subject Name         Mark  Grade    Points   "
line = "=" * len(head)
result += line
print(f"\n{"Grade Point Average(GPA) Report":^{len(head)}}",line,head,line,result,f"Total Points :{tp:.1f}\nTotal Credit :{tc:.1f}\nGrade Point Average(GPA) :{tp / tc:.2f}",sep="\n")

