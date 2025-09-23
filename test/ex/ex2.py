head = ">> Program Calculate Grade <<"
line, result, tc, tp = "=" * len(head), "", 0, 0
print(head,line,"\nInput Data:",sep="\n")
for i in range(6):
    name = input("Enter subject name : ")
    score = int(input("Enter subject score : "))
    print()
    if score >= 80 and score <= 100 : grade, point = "A", 4 * 3
    elif score >= 70 and score <80 : grade, point = "B" , 3 * 3
    elif score >= 60 and score <70 : grade, point = "C" , 2 * 3
    elif score >= 50 and score <60 : grade, point = "D" , 1 * 3
    elif score >=  0 and score <50 : grade, point = "F" , 0 * 3
    result += f":   {i+1}   : {name:<{len("Subject Name                 ")}}: {score:4.1f} :   {grade}   :   {3}   : {point:4.1f} :\n"
    tc += 3
    tp += point
h = ":Sub No.: Subject Name                 : Mark : Grade :Credits:Points:"
l = "=" * len(h)
result += l
print(f"{"Grade Report":>{len(":Sub No.: Subject Name                 :")}}",l,h,l,result,sep="\n")
print(f":{"Total":^{len("Sub No.: Subject Name                 : Mark : Grade ")}}:  {tc:2}   : {tp:4.1f} : ",l,sep="\n")
print(f": {f"Grade Point Average (GPA)  : {tp / tc:.2f}":<{len("ub No.: Subject Name                 : Mark : Grade :Credits:Points")}}:",l,sep="\n")