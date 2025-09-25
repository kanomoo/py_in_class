from random import randint
def data_point():
    datas = {}
    data = ()
    num = int(input("Enter number of student : "))
    for i in range(1,num+1):
        total = 0
        hw = randint(0,30)
        mid = randint(0,35)
        final = randint(0,35)
        total = hw + mid + final
        if total >= 80: grade = "A"
        elif total >= 75: grade = "B+"
        elif total >= 70: grade = "B"
        elif total >= 65: grade = "C+"
        elif total >= 60: grade = "C"
        elif total >= 55: grade = "D+"
        elif total >= 50: grade = "D"
        else: grade = "F"
        data = (hw,mid,final,total,grade)
        datas[i] = data
    return datas

def report(data):
    head = "| No.|  HW(30)  |  MID(35)  | FINAL(35)|TOTAL(100)|GRADE|"
    line = "-" * len(head)
    re = f"{"Report of Sales":^57}"
    print(re,line,head,line,sep="\n")
    for i in data:
        print(f"| {i:2} : {data[i][0]:8.2f} | {data[i][1]:9.2f} | {data[i][2]:8.2f} | {data[i][3]:8.2f} |  {data[i][4]:2} |")
    print(line)
    avgs = ()

    for n in range(0,4):
        total = 0
        for i in data:
            total += data[i][n]
        avg = total / len(data)
        avgs += (avg,)
    print(f"| Avg|{avgs[0]:9.2f} |{avgs[1]:10.2f} |{avgs[2]:9.2f} |{avgs[3]:9.2f} |     |")
    print(line)
data = data_point()
report(data)