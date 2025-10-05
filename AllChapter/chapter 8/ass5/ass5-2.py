#นายปภาวิน ธิติชุณหกุล 6806021612037
from random import randint

def data_std(std):
    datas = []
    for i in range(std):
        hw, mid, final = randint(0,30), randint(0,35), randint(0,35)
        total = sum((hw,mid,final))
        check_grade = {80:"A",75:"B+",70:"B",65:"C+",60:"C",55:"D+",50:"D",0:"F"}
        for i in check_grade:
            if total >= i:
                grade = check_grade[i]
                break
        datas.extend([[hw, mid, final, total, grade]])

    avg = []
    for i in range(len(datas[0]) - 1):
        total  =  0
        for n in range(len(datas)):
            total += datas[n][i]
        avg.append(total / len(datas))
    avg.append("")
    datas.append(avg)

    return datas

def report(data):
    result = ""
    head  = "| No.|  HW(30)  |  MID(35) | FINAL(35)|TOTAL(100)|GRADE|"
    line = "-" * len(head)
    result += f"{"Report of Sales":^{len(head)}}\n{line}\n{head}\n{line}\n"
    for i in range(len(data)):
        if i != (len(data)) - 1: result += f"| {i+1:2} :"
        else: result += f"{line}\n| Avg|"
        for n in range(len(data[0])):
            if n != len(data[0]) -1: result += f"{data[i][n]:9.2f} |"
            else: result += f"{data[i][n]:>4} |"
        result += "\n"
    result += line
    print(result)


def Main():
    std = int(input("Enter number of student : "))
    data = data_std(std)
    report(data)

if __name__ == "__main__":
    Main()