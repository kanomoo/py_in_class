def input_sales():
    from random import randint
    with open("sales.txt","w",encoding="UTF-8") as fout:
        for i in range(15):
            for i in range(7):
                sales = randint(100,5000)
                fout.write(f"{sales}")
                if i < 6:
                    fout.write(f",")
            fout.write("\n")

def data_sales():
    with open("sales.txt") as fin:
        datas = []
        for i in fin:
            i = i.rstrip("\n").split(",")
            total = 0
            for t in i:
                total += int(t)
            i.append(total)
            datas.append(i)
    return datas

def report(datas):
    with open("sales.txt") as fin:
        head = ": No.:"
        for i in range(7):
            head += f"   Day  {i}   :"
        head += "   Total    :"
        line = "-" * len(head)
        print(format("Report of Sales","^110"))
        print(line,head,line,sep="\n")
        n = 0
        mess = ""
        for i in datas:
            n += 1
            mess += f":{n:3} :"
            for d in range(8):
                mess += f"{int(i[d]):11,.2f} :"
            mess += "\n"
        print(mess,line,sep="")
        totals = []
        for i in range(8):
            total = 0
            for t in datas:
                total += int(t[i])
            totals.append(format(total,",.2f"))
        p = "Total:"
        for i in totals:
            p += f"{i:>11} :"
        print(p,line,sep="\n")

input_sales()
datas = data_sales()
report(datas)




# แบบแรก #############################################################################################
# from random import randint
#
# def data_sales():
#     datas = {}
#     for i in range(1,16):
#         data = []
#         total = 0
#         for n in range(7):
#             sales = randint(100,5000)
#             data.append(sales)
#             total += sales
#         data.append(total)
#         datas[i] = data
#     return datas
#
# def report(datas):
#     head = ": No.:   Day  1   :   Day  2   :   Day  3   :   Day  4   :   Day  5   :   Day  6   :   Day  7   :   Total    :"
#     line = "-" * len(head)
#     print(f"{"Report of sales":^110}")
#     print(line,head,line,sep="\n")
#     for i in datas:
#         print(f": {i:2} :",end="")
#         for n in datas[i]:
#             print(f"{n:11,.2f}",end=" :")
#         print()
#     print(line)
#     totals = []
#     for n in range(8):
#         total = 0
#         for i in datas:
#             total += datas[i][n]
#         totals.append(total)
#     print("Total:",end="")
#     for i in totals:
#         print(f"{i:11,.2f}",end=" :")
#     print("\n",line,sep="")
#     return totals
#
# def save_sales(datas,totals):
#     fout = open("sales2.txt","w",encoding="UTF-8")
#     for i in datas:
#         sale = ""
#         for n in range(len(datas[i])-1):
#             sale += f"{datas[i][n]:}"
#             if n < (len(datas[i])-2):
#                 sale += ","
#         sale += "\n"
#         fout.write(sale)
#
# datas = data_sales()
# totals = report(datas)
# save_sales(datas,totals)