# นายปภาวิน ธิติชุณหกุล 6806021612037 it sec.c
result, tc, tp  =  "", 0, 0
num = input("Enter number of courses: ")
while True :
    if num.isdigit(): 
        num = int(num)
        break
    else: 
        print("Invalid number of courses. Please enter a positive integer.")
        num = input("Enter number of courses: ")
for i in range(int(num)):
    name = input(f"#{i+1} course name: ")
    credit = int(input(f"#{i+1} credit (1-4): "))
    while credit < 1 or credit > 4:
        print("Invalid credit. Please enter an integer in 1-4.")
        credit = int(input(f"#{i+1} credit (1-4): "))
    score = int(input(f"#{i+1} score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter an integer in 0-100.")
        score = int(input(f"#{i+1} score (0-100): "))
    if score >= 80 and score <= 100: grade, point = "A" , 4 * credit
    elif score >= 75: grade, point = "B+" , 3.5 * credit
    elif score >= 70: grade, point = "B"  , 3 * credit
    elif score >= 65: grade, point = "C+" , 2.5 * credit
    elif score >= 60: grade, point = "C"  , 2 * credit
    elif score >= 55: grade, point = "D+" , 1.5 * credit
    elif score >= 50: grade, point = "D"  , 1 * credit
    elif score >= 0 and score < 50: grade, point = "F", 0 * credit
    tc += credit
    tp += point
    result += f"|   {i+1} | {name:28}|    {credit}    |   {score:3} |   {grade:<2}  |\n"
head = "|  No |           Course            |  Credit | Score | Grade |"
line = len(head) * "="
l = len(head) * "-" 
print(line,head,l,result+l,f"Total : Credits: {tc}\nGPA: {tp / tc:.2f}",line,sep="\n")