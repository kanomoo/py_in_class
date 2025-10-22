from random import randint

def t1():
    while True:
            choice = input("\nMain Menu\n==========\n 1. Play Game\n 2. Exit\nEnter Choice : ")
            match choice:
                case "1":
                    rd = randint(1,99)
                    print("\nNow Play game")
                    for i in range(6):
                        num = int(input(f"Enter guess number(#{i+1}) : "))
                        if num > rd: print("Your value is more than")            
                        elif num < rd: print("Your value is less than")
                        elif num == rd:
                            print(f"\nYour win, use guess {i+1} times.\nNumber guess is {rd}.")
                            break
                        if i == 5 :print(f"\nYou lose, random number is {rd}.")
                case "2": 
                    print("Exit Program...\n")
                    input("Press any key to continues . . .")
                    exit()
                case _: print("No cohice, enter again.")

def t2():
    head = ">> Program Calucalate Grade <<"
    line = "=" * len(head)
    result = f"{head}\n{line}\n\nInput data:"
    print(result)
    grades = {80:("A",4), 70:("B",3), 60:("C",2), 50:("D",1), 0:("F",0)}
    data = []
    for i in range(6):
        name = input(f"Enter subject name({i+1}) : ")
        score = int(input(f"Enter subject score({i+1}) : "))
        for i in grades:
            if score >= i: 
                grade, point = grades[i]
                break
        credit, points = 3, point * 3
        data.append([name,score,grade,credit,points])
        print()
    head = ":Sub No.: Subject Name               : Mark : Grade :Credits:Points:"
    line = "=" * len(head)
    result2 = f"{"Grade Report":^{len(head)}}\n{line}\n{head}\n{line}\n"
    for i in range(len(data)):
        result2 += f":   {i+1}   : {data[i][0]:27}: {data[i][1]:4.1f} :   {data[i][2]}   :   {data[i][3]}   : {data[i][4]:4.1f} :\n"
    result2 += f"{line}\n:{"Total":^51}:  {sum([i[3] for i in data]):2}   : {sum([i[4] for i in data]):4.1f} :\n{line}\n: Grade Point Average(Gpa) : {sum([i[4] for i in data]) / sum([i[3] for i in data]):4.2f}{":":>35}\n{line}"
    print(result2)

def t3():
    salary = 0
    t_tax = [[1, 150_000, 0],[150_001, 300_000, 5],[300_001, 500_000, 10],[500_001, 750_000, 15],[750_001, 1_000_000, 20],[1_000_001, 2_000_000, 25],[2_000_001, 5_000_000, 30],[0, 5_000_000, 35]]
    while True:
        head = "| Tax Main menu |"
        line = "=" * len(head)
        choice =  input(f"{line}\n{head}\n{line}\n 0. Exit\n 1. Input Salary({salary:,.2f})\n 2. Display Tax\nEnter choice : ")
        match choice:
            case "0":
                print("\nExit Program...")
                exit()
            case "1":
                salary = int(input("Enter salary : "))
            case "2":
                income, discount = salary * 12, 100_000
                net_income = income - discount
                print(f"\nSalary : {salary:,.2f}\nIncome : {income:,.2f}\nDiscount : {discount:,.2f}\nNet Income : {net_income:,.2f}")
                h = "|         Net     Income      |Tax Rate|                 Tax                  |"
                l = "=" * len(h)
                result = f"\nReport Tax:\n{l}\n{h}\n{l}\n"
                t, total_tax = 0, 0
                for r in t_tax:
                    rate = r[2]/100
                    if net_income == 0: break
                    elif net_income > r[1]  - r[0] + 1: t = r[1]  - r[0] + 1
                    elif net_income < r[1]  - r[0] + 1: t = net_income
                    net_income = net_income - t

                    if r[0] == 0: result += f"| {"":12} > {r[1]:12,.2f} |  {r[2]:3}%  |{f"{t:10,.2f} * {rate:.2f}  ":>22}|{t * rate:14,.2f} |\n"
                    else : result += f"| {r[0]:12,.2f} - {r[1]:12,.2f} |  {r[2]:3}%  |{f" {t:10,.2f} * {rate:.2f}  ":>22}|{t * rate:14,.2f} |\n"
                    total_tax += t * rate
                result += f"{l}\n|{"Total Tax":^61}|{total_tax:14,.2f} |\n{l}"
                print(result)
        print()

if __name__ == "__main__":
    t3()