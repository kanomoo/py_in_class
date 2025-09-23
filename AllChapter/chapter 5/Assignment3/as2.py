#นายปภาวิน ธิติชุณหกุล 6806021612037
result,tc,tp = "",0,0
print(">> Program Calculate Grade <<","=" * 29,"\nInput Data:",sep="\n")
for i in range(6):
    name = input(f"Enter subject name({i+1}) : ")
    score = int(input(f"Enter subject score({i+1}) : "))
    print()
    if score >= 80 and score <= 100: grade,points = "A",4*3
    elif score >= 70 and score <= 79: grade,points = "B",3*3
    elif score >= 60 and score <= 69: grade,points = "C",2*3
    elif score >= 50 and score <= 59: grade,points = "D",1*3
    elif score >= 0 and score <= 49: grade,points = "F",0*3
    tc += 3
    tp += points
    result += f":   {i+1}   : {name:<{len("Subject Name               ")}}: {score:4.1f} :   {grade}   :   {3}   : {points:4.1f} :\n"
head = ":Sub No.: Subject Name               : Mark : Grade :Credits:Points:"
line = "=" * len(head) #ใช้ len กับตัวแปร string เพื่อลดเวลาจัด
top = f"{"Grade Report":>{len(":Sub No.: Subject Name  "+"Grade Report")}}"
result += line
print(top,line,head,line,result,sep="\n")
print(f":{"Total":>{len(":Sub No.: Subject Name               ")}}{":":>{len(":Mark : Grade :")}}  {tc}   : {tp:4.1f} :",line,sep="\n")
print(f": {f"Grade Point Average(GPA)  : {tp / tc:4.2f}":{len(head)-3}}:",line,sep="\n")