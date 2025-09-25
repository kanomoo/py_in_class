from random import randint

def data_sales():
    datas = []
    for i in range(15):
        total = 0
        datas.append([])
        for n in range(7):
            rd =  randint(100,5000)
            total += rd
            datas[i].append(rd)
        datas[i].append(total)

    d_totals = []
    for n in range(len(datas[0])):
        d_total = 0
        for i in range(len(datas)):
            d_total += datas[i][n]
        d_totals.append(d_total)
    datas.append(d_totals)
    return datas

def report(data):
    result = ""
    head = ": No.:"
    for i in range(7):
        head += f"   Day  {i+1}   :"
    head += "   Total    :"
    line = "-" * len(head)
    result += f"{"Report of Sales":^{len(head)}}\n{line}\n{head}\n{line}\n"
    for i in range(len(data)):
        if i != len(data) - 1: result += f": {i+1:2} :"
        else: result += f"Total:"
        for n in range(len(data[0])):
            result += f"{data[i][n]:11,.2f} :"
        result += "\n"
    result += line
    print(result)

def Main():
    data = data_sales()
    for i in data:
        print(i)
    report(data)

if __name__ == "__main__":
    Main()


# ===============================================================================


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
    std = 12
    data = data_std(std)
    report(data)

if __name__ == "__main__":
    Main()
#