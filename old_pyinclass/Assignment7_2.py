def std_point():
    from random import randint
    with open("students.txt","w",encoding="UTF-8") as fout:
        for i in range(25):
            hw = randint(0,30)
            mid = randint(0,35)
            final = randint(0,35)
            fout.write(f"{hw},{mid},{final}\n")

def std_data():
    with open("students.txt") as fin:
        datas = []
        for i in fin:
            total = 0
            i = i.rstrip("\n").split(",")
            for t in i:
                total += int(t)
            i.append(total)
            g = {80:"A",75:"B+",70:"B",65:"C+",60:"C",55:"D+",50:"D",0:"F"}
            for n in g:
                if total > n:
                    grade = g[n]
                    break
            i.append(grade)
            datas.append(i)
        return datas

def report(datas):
    head = "| No.|  HW(30)  |  MID(35)  | FINAL(35) |TOTAL(100) |GRADE|"
    line = "-" * len(head)
    print(format("Report of Student","^59"))
    print(line,head,line,sep="\n")
    n = 0
    for i in datas:
        n += 1
        print(f"|{n:3} :{int(i[0]):9.2f} |{int(i[1]):10.2f} |{int(i[2]):10.2f} |{int(i[3]):10.2f} |{i[4]:>4} |")
    print(line)
    avg = []
    for n in range(4):
        total = 0
        for a in datas:
            total += int(a[n])
        avg.append(format(total/25,".2f"))
    print(f"| Abg|{avg[0]:>9} |{avg[1]:>10} |{avg[2]:>10} |{avg[3]:>10} |     |")
    print(line)

std_point()
datas = std_data()
report(datas)
#






#แบบ txt ผิด ##########################################################################################
# def data_std():
#     from random import randint
#     with open("students.txt","w",encoding="UTF-8") as fout:
#         for i in range(25):
#             hw = randint(0,30)
#             mid = randint(0,35)
#             final = randint(0,35)
#             total = hw + mid + final
#             if total >= 80: grade = "A"
#             elif total >= 75: grade = "B+"
#             elif total >= 70: grade ="B"
#             elif total >= 65: grade ="C+"
#             elif total >= 60: grade ="C"
#             elif total >= 55: grade ="D+"
#             elif total >= 50: grade ="D"
#             else: grade = "F"
#             fout.write(f"{hw}, {mid}, {final}, {total}, {grade}\n")
#
# def data_total():
#     fin = open("students.txt")
#     data = []
#     for i in fin:
#         i = i.rstrip("\n").split(",")
#         data.append(i)
#     totals = []
#     for i in range(4):
#         total = 0
#         for n in data:
#             total += int(n[i])
#         totals.append(total/25)
#     return(totals)
#
# def report(totals):
#     head = "| No.|  HW(30)  |  MID(35) | FINAL(35) |TOTAL(100)|GRADE|"
#     line = "-" * len(head)
#     print(format("Report of Student","^57"))
#     print(line,head,line,sep="\n")
#     n = 0
#     with open("students.txt") as fin:
#         for i in fin:
#             n += 1
#             i = i.rstrip("\n").split(",")
#             print(f"|{n:3} :{int(i[0]):9.2f} |{int(i[1]):9.2f} |{int(i[2]):10.2f} |{int(i[3]):9.2f} |{i[4]:>4} |")
#         print(line)
#         print(f"| Avg|{float(totals[0]):9.2f} |{float(totals[1]):9.2f} |{float(totals[2]):10.2f} |{float(totals[3]):9.2f} |     |")
#         print(line)
#
# data_std()
# totals = data_total()
# report(totals)
