#นายปภาวิน ธิติชุณหกุล 6806021612037
def add_sccore():
    print("\nAdd Score of Student.")
    pj = int(input("Enter score project : "))
    hw = int(input("Enter score homework : "))
    md = int(input("Enter score midterm : "))
    fn = int(input("Enter score final : "))
    with open(r"AllChapter/chapter 9/assignment6/02/Score.txt","a") as fin:
        fin.write(f"{pj},{hw},{md},{fn}\n")
    print("Save data already.")

def report_score():
    head = "| No.|Project(15)|  HW(25)   |  MID(30)  | FINAL(30) |TOTAL(100) |GRADE|"
    line = "-" * len(head)
    result = f"\n{"Reprot Grade of Student":^{len(head)}}\n{line}\n{head}\n{line}\n"
    with open(r"AllChapter/chapter 9/assignment6/02/Score.txt","r") as fout:
        datas = []
        for i in fout:
            data = [int(n) for n in i.strip("\n").split(",") ]
            total = sum(data)
            data.append(total)
            grades = {80:"A",75:"B+",70:"B",65:"C+",60:"C",55:"D+",50:"D",0:"F"}
            for point in grades:
                if total >= point: 
                    data.append(grades[point])
                    break
            datas.append(data)

    data = []
    for n in range(len(datas[0])-1):
        total = 0
        for i in range(len(datas)):
            total += datas[i][n]
        data.append(total / len(datas))
    data.append(0)
    datas.append(data)

    for i in range(len(datas)):
        if i < len(datas) - 1 :
            result += f"| {i+1:2} :"
        else: result += f"{line}\n| Avg|"
        for n in range(len(datas[0])):
            if n < len(datas[0]) - 1:
                result += f"{datas[i][n]:10.2f} |"
            else: 
                if datas[i][n] != 0:
                    result += f"  {datas[i][n]:<2} |\n"
                else: result += f"  {"":<2} |\n"
    print(result+line)