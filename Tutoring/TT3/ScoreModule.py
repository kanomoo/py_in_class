def add_score(file):
    id = input("\nAdd Score of Student.\nEnter id : ")
    p = input("Enter Score project : ")
    h = input("Enter score homework : ")
    m = input("Enter score midterm : ")
    f = input("Enter score final : ")
    print("Save data already.")
    with open(file,"a",encoding="utf-8") as fin:
        fin.write(",".join((p,h,m,f))+"\n")

def report_score(file):
    data = []
    with open(file,"r",encoding="utf-8") as fout:
        for i in fout:
            data.append([int(n) for n in  i.strip("\n").split(",")])
    head = "| No.|    ID     |Project(15)|  HW(25)   |  MID(30)  | FINAL(30) |TOTAL(100) |GRADE|"
    line = "=" * len(head)
    result = f"{"Report Grade of Student":^{len(head)}}\n{line}\n{head}\n{line}\n"
    totals = 0
    grades = {80:"A",75:"B+",70:"B",65:"C+",60:"C",55:"D+",50:"D",0:"F"}
    for i in range(len(data)):
        result += f"| {i+1:2} :"
        for n in data[i]:
            result += f"{n:10.2f} |"
        result += f"{sum(data[i]):10.2f} |"
        totals += sum(data[i])
        for g in grades:
            if sum(data[i]) >= g: 
                grade = grades[g]
                break
        result += f"  {grade:2} |\n"
    total = []
    for n in range(len(data[0])):
        t = 0
        for i in range(len(data)):
            t += int(data[i][n])
        total.append(t)
    result += f"{line}\n| Avg|"
    for i in total:
        result += f"{int(i) / len(data):10.2f} |"
    result += f"{totals / len(data):10.2f} |     |\n{line}"
    print(result)

def edit_score(file):
    data = []
    with open(file,"r",encoding="utf-8") as fout:
        for i in fout:
            data.append([n for n in  i.strip("\n").split(",")])
    id = input("Enter id : ")
    for i,v in enumerate(data):
        if id in data[0]:
            p = input("Enter Score project : ")
            h = input("Enter score homework : ")
            m = input("Enter score midterm : ")
            f = input("Enter score final : ")
            data[i] = id,p,h,m,f
            with open(file,"w",encoding="utf-8") as fin:
                for i in range(len(data)):
                    fin.write(",".join(data[i])+"\n")
            break
    



def del_score(file):
    data = []
    with open(file,"r",encoding="utf-8") as fout:
        for i in fout:
            data.append([n for n in  i.strip("\n").split(",")])
    id = input("Enter id : ")
    for i,v in enumerate(data):
        if id in data[0]:
            del data[i]
            with open(file,"w",encoding="utf-8") as fin:
                for i in range(len(data)):
                    fin.write(",".join(data[i])+"\n")
            break