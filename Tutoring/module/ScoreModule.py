from random import randint as rd

def add_score(file):
    print("Add Score student.")
    p = (input("Enter score project : "))
    h = (input("Enter score homework : "))
    m = (input("Enter score midterm : "))
    f = (input("Enter score final : "))
    with open(file,"a",encoding="utf-8") as fin:
        fin.write(",".join((p,h,m,f))+"\n")
    print("Save data already.")

def report_score(file):
    data = []
    grades = {80:"A", 75:"B+", 70:"B", 65:"C+", 60:"C", 55:"D+", 50:"D", 0:"F"}
    with open(file,"r",encoding="utf-8") as fout:
        for i in fout:
            data.append([int(n) for n in i.strip("\n").split(",")])

    head = f"| No.|Project(15)|  HW(25)   |  MID(30)  | FINAl(30) |TOTAL(100) |GRADE|"
    line = "=" * len(head)
    result = f"{line}\n{head}\n{line}\n"
    totals = 0
    for i in range(len(data)):
        result += f"| {i+1:2} :"
        for n in data[i]:
            result += f"     {n:5,.2f} |"
        result += f"     {sum(data[i]):5,.2f} |"
        totals += sum(data[i])
        for j in grades:
            if sum(data[i]) >= j: 
                grade = grades[j]
                break
        result += f"  {grade:2} |"
        result += "\n"
    result += f"{line}\n| Avg|"
    for i in range(len(data[0])):
        result += f"     {sum([n[i] for n in data]) / len(data):5,.2f} |"
    result += f"     {totals / len(data):5,.2f} |"
    result += f"     |\n{line}"

    print(result)