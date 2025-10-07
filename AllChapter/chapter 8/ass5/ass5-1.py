#นายปภาวิน ธิติชุณหกุล 6806021612037
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
        else: result += f"{line}\nTotal:"
        for n in range(len(data[0])):
            result += f"{data[i][n]:11,.2f} :"
        result += "\n"
    result += line
    print(result)

def Main():
    data = data_sales()
    report(data)

if __name__ == "__main__":
    Main()