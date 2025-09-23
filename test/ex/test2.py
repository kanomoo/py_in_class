head = ">> Program Calculate Grade <<"
line, result, tc, tp = "=" * len(head), "", 0, 0
print(line,head,line,"\nInput Data:",sep="\n")
for i in range(6):
    name = input(f"Enter Subject name({i+1}) : ")
    score = int(input(f"Enter subject score({i+1}) : "))
    print()
    if score >= 80 and score <= 100: grade, point = "A", 4 * 3
    elif score >= 70 and score <=79: grade, point = "B", 3 * 3
    elif score >= 60 and score <=69: grade, point = "C", 2 * 3
    elif score >= 50 and score <=59: grade, point = "D", 1 * 3
    elif score >= 0 and score <=49: grade, point = "F", 0
    tc += 3
    tp += point
    result += f":   {i+1}   : {name:<{len("Subject Name               ")}}: {score:4.1f} :    {grade}  :   {3}   : {point:4.1f} :\n"
h = ":Sub No.: Subject Name               : Mark : Grade :Credits:Points:"
l = "=" * len(h)
result += l
print(f"{"Grade Report":>{len(":Sub No.: Subject Name  Grade Report")}}",l,h,l,result,sep="\n")
print(f":{"Total":>{len("Sub No.: Subject Name                ")}}{":":>{len("   1.0 :    F  ")}}  {tc:2}   : {tp:4.1f} :")
print(l,f": {f"Grade Point Average(GPA) : {tp / tc:.2f}":<{len("                               Total              :  18   :  0.0 ")}}:",l,sep="\n")