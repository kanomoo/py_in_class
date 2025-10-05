#นายปภาวิน ธิติชุณหกุล 6806021612037
from random import randint
def random_and_save(filename = r"AllChapter/chapter 9/assignment6/01/Sale.txt",no = 15,day = 7):
    with open(filename,"w") as fin:
        for i in range(no):
            sale = []
            for n in range(day): 
                sale.append(randint(500,5000))
            fin.write(",".join([str(i) for i in sale])+"\n")

def report_sale(filename = r"AllChapter/chapter 9/assignment6/01/Sale.txt"):
    with open(filename,"r") as fout:
        datas = []
        for i in fout:
            data = []
            for n in i.split(","):
                data.append(int(n))
            data.append(sum(data))
            datas.append(data)
    data = []
    for n in range(len(datas[0])):
        total = 0
        for i in range(len(datas)):
            total += (datas[i][n])
        data.append(total)
    datas.append(data)

    head = ": No.:"
    for i in range(len(datas[0]) - 1): head += f"   Day {i+1:2}   :"
    head += "   Total    :"
    line = "-" * len(head)
    result = f"{"Report of Sales":^{len(head)}}\n{line}\n{head}\n{line}\n"
    for i in range(len(datas)):
        if i < len(datas) - 1:
            result += f": {i+1:2} :"
        else: result += f"{line}\nTotal:"
        for n in range(len(datas[i])):
            result += f" {datas[i][n]:>10,.2f} :"
        result += "\n"
    print(result+line)