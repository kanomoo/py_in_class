# from random import randint, choice, uniform
def add_and_save(filename):
    id = input("Enter Id : ")
    price = input("Enter Price : ")
    dpi = input("Enter dpi : ")
    term = input("Enter term : ")
    per = input("Enter per : ")
    with open(filename,"a",encoding="utf-8") as fin:
        fin.write(",".join((id,price,dpi,term,per))+"\n")
        # for i in range(6):
        #     fin.write(",".join((str(randint(320000,1300000)),str(randint(10,25)),str(choice((48,60,72,84))),format((uniform(2.20,5.50)) ,".2f")))+"\n")

def report_installment(filename):
    data = []
    with open(filename,"r",encoding="utf-8") as fout:
        for i in fout:
            data.append([float(n) if i != 0 else str(n) for i,n in enumerate(i.strip("\n").split(","))])
    n = 0
    head = f"| No.|{"ID":^14}|{"Price":^14}|{"DP":^14}|{"Dp Amt":^14}|{"Fin Amt":^14}|{"Int":^14}|{"Term":^14}|{"Tot Int":^14}|{"Net Amt":^14}|{"Install":^14}|"
    line = "=" * len(head)
    result = f"{"Report Installment":^{len(head)}}\n{line}\n{head}\n{line}\n"
    for i in data:
        n += 1
        id, price, dpi, term, per = i[0] ,i[1], i[2], i[3], i[4]
        dp = price * dpi/100
        fin = price - dp 
        i_r = per / 12
        i_a = fin * (i_r/100) * term
        net = fin + i_a
        ins = net / term
        result += f"| {n:2} |{id:>13} |{price:13,.2f} |{dpi:13} |{dp:13,.2f} |{fin:13,.2f} |{per:13,.2f} |{term:13,.2f} |{i_a:13,.2f} |{net:13,.2f} |{ins:13,.2f} |\n"
    print(result+line)

def edit_installment(file):
    data = []
    with open(file,"r",encoding="utf-8") as fout:
        for i in fout:
            data.append(i.strip("\n").split(","))

    id = input("Enter Id : ")
    for i,v in enumerate(data):
        if id in v[0]:
            price = input("Enter Price : ")
            dpi = input("Enter dpi : ")
            term = input("Enter term : ")
            per = input("Enter per : ")
            data[i] = [id,price,dpi,term,per]
            break
    else: print("Id not found")

    with open(file,"w",encoding="utf-8") as fin:
        for i in data:
            fin.write(",".join(i)+"\n")
    print("Data save")

def del_installment(file):
    data = []
    with open(file,"r",encoding="utf-8") as fout:
        for i in fout:
            data.append(i.strip("\n").split(","))

    id = input("Enter Id : ")
    for i,v in enumerate(data):
        if id in v[0]: del data[i]
    
    with open(file,"w",encoding="utf-8") as fin:
        for i in data:
            fin.write(",".join(i)+"\n")
    print("Data deleted")