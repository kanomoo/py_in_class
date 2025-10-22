from random import randint, choice, uniform
def random_and_save(filename):
    with open(filename,"w",encoding="utf-8") as fin:
        for i in range(6):
            fin.write(",".join((str(randint(320000,1300000)),str(randint(10,25)),str(choice((48,60,72,84))),format((uniform(2.20,5.50)) ,".2f")))+"\n")

def report_installment(filename):
    data = []
    with open(filename,"r",encoding="utf-8") as fout:
        for i in fout:
            data.append([float(n) for n in i.strip("\n").split(",")])
    n = 0
    head = f"| No.|{"Price":^14}|{"DP":^14}|{"Dp Amt":^14}|{"Fin Amt":^14}|{"Int":^14}|{"Term":^14}|{"Tot Int":^14}|{"Net Amt":^14}|{"Install":^14}|"
    line = "=" * len(head)
    result = f"{"Report Installment":^{len(head)}}\n{line}\n{head}\n{line}\n"
    for i in data:
        n += 1
        price, dpi, term, per = i[0], i[1], i[2], i[3]
        dp = price * dpi/100
        fin = price - dp 
        i_r = per / 12
        i_a = fin * (i_r/100) * term
        net = fin + i_a
        ins = net / term
        result += f"| {n:2} |{price:13,.2f} |{dpi:13} |{dp:13,.2f} |{fin:13,.2f} |{per:13,.2f} |{term:13,.2f} |{i_a:13,.2f} |{net:13,.2f} |{ins:13,.2f} |\n"
    print(result+line)