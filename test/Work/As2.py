#ข้อ 2 สันติชัย ไชยมโน 6806021612401
head = ">>  Program Calculate Grade <<"
line, result,tc, tp = len(head) * "=", "", 0, 0
print(head,line,"\nInput Data:",sep="\n")
for i in range(6):
    name = input(f"Enter subject name ({i+1}) : ")
    score = int(input(f"Enter subject score ({i+1}) : "))
    print()
    if score >= 80 and score <= 100: grade, point = "A", 4 * 3
    elif score >= 70: grade, point = "B", 3 * 3
    elif score >= 60: grade, point = "C", 2 * 3
    elif score >= 50: grade, point = "D", 1 * 3
    elif score >=  0: grade, point = "F", 0 * 3
    tc += 3
    tp += point
    result += f":   {i+1}   : {name:<26}:{score:5.1f} :   {grade}   :   {3}   : {point:4.1f} :\n"
h = ":Sub No.: Subject Name              : Mark : Grade :Credits:Points:"
l = len(h) * "="
print(f"{"Grade Report":>36}",l,h,l,result+l,sep="\n")
print(f":{"Total":>36}{" "*len(" Mark : Grade ")}:  {tc:2}   : {tp:4.1f} :",l,sep="\n")
print(f": {f"Grade Point  Average(GPA) : {tp / tc:.2f}":64}:",l,sep="\n")