head = ": Program Cal Grade :"
line, total, Min, Max, result = len(head) * "=", 0, 100, 0, ""
print(line,head,line,sep="\n")
for i in range(5):
    score = int(input(f"Enter score #{i+1} : "))
    while score < 0 or score > 100:
        print("error")
        score = int(input(f"Enter score #{i + 1} : "))
    if score >= 80 and score <= 100: grade = "A"
    elif score>=70 and score <80: grade = "B"
    elif score>=60 and score <70: grade = "C"
    elif score>=50 and score <60: grade = "D"
    elif score>= 0 and score <50: grade = "F"
    result += f"|  {i+1}  |   {score:2}  |   {grade}   |\n"
    total += score
    if score > Max: Max = score
    if score < Min: Min = score
h = "| No. | Score | Grade |"
l = f"+{"=" * (len(h)-2)}+"
print("\n    Report Grade",l,h,l,result+l,f"|Average Score| {total / 5:5.2f} |\n|Maximum Score| {Max:5} |\n|Minimum Score| {Min:5} |",l,sep="\n")