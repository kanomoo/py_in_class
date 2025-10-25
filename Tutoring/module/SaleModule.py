from random import randint as rd

def random_and_save_sale(file,column,row):
    with open(file,"w",encoding="utf-8") as fin:
        for i in range(column):
            data = []
            for n in range(row):
                data.append(str(rd(500,5000)))
            fin.write(",".join(data)+"\n")

def report(file):
    data = []
    with open(file,"r",encoding="utf-8") as fout:
        for i in fout:
            data.append([int(n) for n in i.strip("\n").split(",")])
    head = ": No.:"
    for i in range(len(data[0])):
        head += f"   Day  {i+1:2}  :"
    head += f"   Total    :"
    line = "=" * len(head)
    result = f"{"Reprot of Sales":^{len(head)}}\n{line}\n{head}\n{line}\n"
    totals = 0
    for i in range(len(data)):
        result += f"| {i+1:2} :"
        for n in data[i]:
            result += f"   {n:8,.2f} :"
        totals += sum(data[i])
        result += f"  {sum(data[i]):8,.2f} :"
        result += "\n"
    result += f"{line}\nTotal:"
    for n in range(len(data[0])):
        total = 0
        for i in range(len(data)):
            total += data[i][n]
        result += f"  {total:8,.2f} :"
    result += f" {totals:9,.2f} :\n{line}"
    print(result)