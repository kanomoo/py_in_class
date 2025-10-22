from random import randint
def t1():
    def data2():
        data = []
        for i in range(15):
            s_data = []
            for n in range(7):
                s_data.append(randint(100,5000))
            data.append(s_data)
            data[i].append(sum(s_data))

        d_total = []
        for n in range(len(data[i])):
            total = 0
            for i in range(len(data)):
                total += data[i][n]
            d_total.append(total)
        data.append(d_total)
        return data

    def main():
        data = data2()
        head = ": No.:"
        for i in range(7):
            head += f"   Day  {i+1}   :"
        head += "   Total    :"
        line = "=" * len(head)
        result = f"{"Reprot of Sales":^{len(head)}}\n{line}\n{head}\n{line}\n"
        for i in range(len(data)):
            if i != 15:
                result += f": {i+1:2} :"
                for n in range(len(data[i])):
                    result += f" {data[i][n]:10,.2f} :"
            else:
                result += f"{line}\nTotal:"
                for n in range(len(data[i])):
                    result += f" {data[i][n]:10,.2f} :"
            result += "\n"
        print(result+line)

    if __name__ == "__main__":
        main()

def t2():
    def data2(num):
        grades = {80:"A", 75:"B+", 70:"B", 65:"C+", 60:"C", 55:"D+", 50:"D", 0:"F"}
        datas = []
        for i in range(num):
            data = [randint(0,30),randint(0,35),randint(0,35)]
            total = sum(data)
            for i in grades:
                if total >= i: 
                    grade = grades[i]
                    break
            data.extend((total,grade))
            datas.append(data)
        return datas
    
    def report():
        num = int(input("Enter number of student : "))
        data = data2(num)
        head = "| No.|  HW(30)  |  MID(35) | FINAL(35)|TOTAL(100)|GRADE|"
        line = "=" * len(head)
        result = f"{"\nReport of Sales":^{len(head)}}\n{line}\n{head}\n{line}\n"
        n = 0
        for i in data:
            n += 1
            result += f"| {n:2} :    {i[0]:5.2f} |    {i[1]:5.2f} |    {i[2]:5.2f} |    {i[3]:5.2f} |  {i[4]:2} |\n"
        result += f"{line}\n| Avg|    {sum([i[0] for i in data]) / num:5.2f} |    {sum([i[1] for i in data]) / num:5.2f} |    {sum([i[2] for i in data]) / num:5.2f} |    {sum([i[3] for i in data]) / num:5.2f} |     |\n{line}\n"
        print(result)

    if __name__ == "__main__":
        report()

if __name__ == "__main__":
    t2()