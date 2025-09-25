from numpy.ma.core import append


def s():
    print("===9===")#################################################################
    # การสร้างทูเพิล
    # สมาชิกในทูเพิลอาจเป็นข้อมูลชนิดเดียวกันหรือต่างชนิดกันก็ได้
    # สำหรับการกำหนดค่าสมาชิกให้แก่ทูเพิล
    # วิธีที่ง่ายและสะดวกคือ
    # การใช้เครื่องหมายวงเล็บ()
    # หรือใช้ฟังก์ชัน
    # tuple()

    A = () # emptry tuple
    B = (0, 1, 2)
    C = tuple((10, 20, 30))
    D = (5) # variable int no tuple
    D = (5,)
    E = ("Somchai", 'IT', 20, 3.00)

    print("\n===10===")#################################################################
    Num =(1, 3, 5, 7, 9)
    for n in range(5):
        print(Num[n])

    Colors = ("red", "Green", "blue")
    for c in Colors:
        print(c)

    print("\n===12===")#################################################################
    def Check_Point(grade):
        point = 0
        if grade == "A" : point = 4
        elif grade == "B" : point = 3
        elif grade == "C" : point = 2
        elif grade == "D" : point = 1
        elif grade == "F" : point = 0
        return(point)

    # Done = True
    # while Done:
    #     grade = input("Enter grade (Q-ext) : ")
    #     grade = grade.upper() # upper คืนค่าเป็นตัวพิมพ์ใหญ่
    #     if grade == "Q":
    #         Done = False
    #     else:
    #         value = Check_Point(grade)
    #         print(f"Point value of {grade} is {value}")
    #
    # print("End Program.")

    # #ทำแบบง่าย 1
    # count = 0
    # while True:
    #     grade = ["a","A","D","c","b","B","q"]
    #     print(f"Enter grade(Q-exit) : {grade[count]}")
    #     grade[count] = grade[count].upper()
    #     if grade[count] == "Q":
    #         print("End Program.")
    #         break
    #     elif grade[count] == "A": value = 4
    #     elif grade[count] == "B": value = 3
    #     elif grade[count] == "C": value = 2
    #     elif grade[count] == "D": value = 1
    #     elif grade[count] == "F": value = 0
    #     print(f"Point value of {grade[count]} is {value}")
    #     count += 1

    # # ทำแบบง่าย 2
    # def Check_Point(grade):
    #     point = 0
    #     if grade == "A": point = 4
    #     elif grade == "B": point = 3
    #     elif grade == "C": point = 2
    #     elif grade == "D": point = 1
    #     elif grade == "F": point = 0
    #     return(point)
    # while True:
    #     grade = input("Enter grade (Q-exit) : ")
    #     grade = grade.upper()
    #     if grade == "Q": break
    #     else:
    #         point = Check_Point(grade)
    #         print(f"Point value of {grade} is {point}")
    # print("End Program.")

    # # ทำแบบ tuple
    # def Check_Point(grade):
    #     grades = ("A","B","C","D","F")
    #     values = (4, 3, 2, 1, 0)
    #     for i in range(len(grades)):
    #         if grade == grades[i]:
    #             return values[i]
    #
    # while True:
    #     grade = input("Enter grade (Q-exit) : ")
    #     grade = grade.upper()
    #     value = Check_Point(grade)
    #     if grade == "Q":
    #         print("End Program.")
    #         break
    #     else :print(f"Point value of {grade} is {value}")


    # ทำไว้ show ใน terminal
    count = 0
    Done = True
    while Done:
        grade = ["a","A","D","c","b","B","q"]
        print(f"Enter grade (Q-ext) : {grade[count]}")
        grade[count] = grade[count].upper() # upper คืนค่าเป็นตัวพิมพ์ใหญ่
        if grade[count] == "Q":
            Done = False
        else:
            value = Check_Point(grade[count]) #ทำแบบนี้จะโชวค่าเดียวแค่ value ไม่เหมือนการเปิด function เลย
            print(f"Point value of {grade[count]} is {value}") #ทำแบบนี้จะโชวค่าเดียวแค่ value
        count += 1

    print("End Program.")

    print("\n===14===")#################################################################
    def Check_Point(grade):
        grades = ("A", "B", "C", "D", "F")
        values = (4, 3, 2, 1, 0)
        for n in range(len(grades)):
            if grade == grades[n]:
                return(values[n])

    count = 0
    Done = True
    while Done:
        grade = ["a", "A", "D", "c", "b", "B", "q"]
        print(f"Enter grade (Q-ext) : {grade[count]}")
        grade[count] = grade[count].upper()  # upper คืนค่าเป็นตัวพิมพ์ใหญ่
        if grade[count] == "Q":
            Done = False
        else:
            value = Check_Point(grade[count])  # ทำแบบนี้จะโชวค่าเดียวแค่ value ไม่เหมือนการเปิด function เลย
            print(f"Point value of {grade[count]} is {value}")  # ทำแบบนี้จะโชวค่าเดียวแค่ value
        count += 1

    print("End Program.")

    print("\n===15===")#################################################################
    # การใช้โอเปอเรเตอร์และฟังก์ชันร่วมกับทูเพิล
    # โอเปอเรเตอร์ที่สามารถใช้ร่วมกับ
    # ทูเพิล(tuple)
    # ได้
    # ได้แก่:
    # +: การต่อทูเพิล
    # +=: การเพิ่มสมาชิกให้กับทูเพิล(สร้างทูเพิลใหม่)
    # *: การทำซ้ำทูเพิล
    # in: ตรวจสอบว่าสมาชิกอยู่ในทูเพิลหรือไม่
    # not in: ตรวจสอบว่าสมาชิกไม่อยู่ในทูเพิล
    # ==: ตรวจสอบว่าทูเพิลเท่ากันหรือไม่
    # !=: ตรวจสอบว่าทูเพิลไม่เท่ากัน
    # ฟังก์ชันแบบ
    # Built - in ที่สามารถใช้ร่วมกับทูเพิล
    # ได้แก่:
    # len(): หาจำนวนสมาชิกในทูเพิล
    # max(): หาค่าสูงสุดในทูเพิล
    # min(): หาค่าต่ำสุดในทูเพิล
    # sum(): หาผลรวมของค่าตัวเลขในทูเพิล

    A = (1, 3)
    B = (2, 4)
    C = A + B # การบวก tuple 2 tuple
    print(C)
    C += (5, 6, 7, 8) # เพิ่มข้อมูลใน tuple
    print(C)

    if 3 in C: # ถ้า 3 อยู๋ใน tuple C
        print("3 in Tuple")

    if 0 not in C: # ถ้า 0 ไม่อยู่ใน C
        print("0 not in Tuple C")

    print("\n===16===")#################################################################
    D = (2,) * 4 # ทำซ้ำ 2 4 ตัว ต้องมี , เพื่อให้รู้ว่าเป็น tuple
    print(D)
    count = len(C)
    print(f"Tuple C has {count} elements") # นับจำนวนค่าทั้งหมดใน tuple
    count = len(D)
    print(f"Tuple D has {count} elements") # นับจำนวนค่าทั้งหมดใน tuple
    print(sum(C)) # บวกค่าทั้งหมดใน tuple
    print(max(C)) # หาค่า max ใน tuple
    print(min(C)) # หาค่า min ใน tuple

    print("\n===17===")#################################################################
    # def check_rate(total):
    #     if total > 20000: return(0.10)
    #     elif total > 10000: return(0.075)
    #     elif total > 5000: return(0.05)
    #     elif total > 1000: return(0.025)
    #     else : return(0.0)
    #
    # # ประกาศตัวแปร global ก่อนฟังก์ชัน
    #
    #
    # def get_sale():
    #     global sales  # ประกาศ global ในฟังก์ชัน
    #     for n in range(1, 8):
    #         sale = float(input(f"Enter sale day {n} : "))
    #         sales += (sale,)
    #
    # def sum_sale():
    #     total = 0
    #     for n in range(len(sales)):
    #         total += sales[n]
    #     return(total)
    #
    # def report():
    #     print(f"\nTotal sale : {total_sale:,.2f}")
    #     print(f"Commission rate : {rate * 100:.2f}%")
    #     print(f"Total commission : {commission:.2f}")
    #
    # global sales # global (ตัวแปรระดับนอกฟังก์ชัน) แทนที่จะสร้างตัวแปรใหม่ในระดับ local (ภายในฟังก์ชันนั้น) ที่มีปัญหา เพราะสร้าง function ครอบ function
    # sales = ()
    # get_sale()
    # total_sale = sum_sale()
    # rate = check_rate(total_sale)
    # commission = total_sale * rate
    # report()

    # # ทำแบบง่าย
    # total = 0
    # rate = 0
    # for i in range(1,8):
    #     sale = int(input(f"Enter sale day {i} : "))
    #     total += sale
    # if total > 20000 : rate = 0.10
    # elif total > 10000: rate = 0.075
    # elif total > 5000: rate = 0.05
    # elif total > 1000: rate = 0.025
    # else: total = 0
    # print(f"\nTotal sale : {total:,.2f}")
    # print(f"Commission rate : {rate * 100:.2f}%")
    # print(f"Total commission : {total * rate:.2f}")

    # ทำแบบง่าย2
    # def check_rate(total):
    #     if total > 20000: rate = 0.10
    #     elif total > 10000: rate = 0.075
    #     elif total > 5000: rate = 0.05
    #     elif total > 1000: rate = 0.025
    #     else: rate = 0
    #     return rate
    #
    # def get_sale():
    #     global sales
    #     for i in range(1,8):
    #         sale = float(input(f"Enter sale day {i} : "))
    #         sales += (sale,)
    #
    # def sum_sale():
    #     total = 0
    #     for i in range(len(sales)):
    #         total += sales[i]
    #     return total
    #
    # def report():
    #     print(f"\nTotal sale : {total:.2f}")
    #     print(f"Commission rate : {rate * 100:.2f}%")
    #     print(f"Total commission : {total * rate:.2f}")
    #
    # global sales
    # sales = ()
    # get_sale()
    # total = sum_sale()
    # rate = check_rate(total)
    # report()

    # # ทำแบบง่าย 3
    # def check_rate(total):
    #     if total > 20000 : return 0.10
    #     elif total > 10000: return 0.075
    #     elif total > 5000: return 0.05
    #     elif total > 1000: return 0.025
    #     else: return 0
    #
    # def get_sale():
    #     global sales
    #     for i in range(1,8):
    #         sale = float(input(f"Enter sale day {i} : "))
    #         sales += (sale,)
    #     return sales
    #
    # def sum_sale():
    #     total = 0
    #     for i in range(len(sales)):
    #         total += sales[i]
    #     return total
    #
    # def report():
    #     print(f"\nTotal sale : {sum_sale():.2f}")
    #     print(f"Commission rate : {check_rate(sum_sale()) * 100:.2f}%")
    #     print(f"Total commission : {sum_sale() * check_rate(sum_sale())}")
    #
    # global sales
    # sales = ()
    # get_sale()
    # report()

    #ทำไว้ show ใน terminal
    def check_rate(total):
        if total > 20000 : return 0.10
        elif total > 10000: return 0.075
        elif total > 5000: return 0.05
        elif total > 1000: return 0.025
        else: return 0

    def get_sale():
        global sales
        sale = (100, 200, 300, 400, 500, 600 ,700)
        for i in range(1,8):
            print(f"Enter sale day {i} : {sale[i-1]}")
            sales += (sale[i-1],)
        return sales

    def sum_sale():
        total = 0
        for i in range(len(sales)):
            total += sales[i]
        return total

    def report():
        print(f"\nTotal sale : {sum_sale():.2f}")
        print(f"Commission rate : {check_rate(sum_sale()) * 100:.2f}%")
        print(f"Total commission : {sum_sale() * check_rate(sum_sale())}")

    global sales
    sales = ()
    get_sale()
    report()

    print("\n===21===")  #################################################################
    # แก้ไขฟังก์ชัน check_rate โดยใช้ tuple มาทำงาน

    # def check_rate(total):
    #     rates = (0.10, 0.075, 0.05, 0.025, 0.0)
    #     total_sales = (20000.0, 10000.0, 5000.0, 1000, 1.0)
    #     for i in range(len(rates)):
    #         if total > total_sales[i]:
    #             return rates[i]
    #
    # def get_sale():
    #     global sales
    #     for i in range(1,8):
    #         sale = float(input(f"Enter sale day {i} : "))
    #         sales += (sale,)
    #     return sales
    #
    # def sum_sale():
    #     total = 0
    #     for i in range(len(sales)):
    #         total += sales[i]
    #     return total
    #
    # def report():
    #     print(f"\nTotal sale : {sum_sale():.2f}")
    #     print(f"Commission rate : {check_rate(sum_sale()) * 100:.2f}%")
    #     print(f"Total commission : {sum_sale() * check_rate(sum_sale()):.2f}")
    #
    # sales = ()
    # get_sale()
    # report()

    # ทำไว้ show ใน terminal
    def check_rate(total):
        rate = (0.10, 0.075, 0.05, 0.025, 0)
        total_sales = (20000, 10000, 5000, 1000, 1)
        for i in range(len(rate)):
            if total > total_sales[i]:
                return rate[i]

    def get_slae():
        global sales
        sale = (100, 200, 300, 400 ,500 ,600 ,700)
        for i in range(1,8):
            print(f"Enter asle day {i} : {sale[i-1]}")
            sales += (sale[i-1],)
        return sales

    def sum_sale():
        total = 0
        for i in range(len(sales)):
            total += sales[i]
        return total

    def report():
        print(f"\nTotal sale : {sum_sale():.2f}")
        print(f"Commission rate : {check_rate(sum_sale()) * 100:.2f}%")
        print(f"Total commission : {sum_sale() * check_rate(sum_sale()):.2f}")

    sales = ()
    get_slae()
    report()

    print("\n===22===")  #################################################################
    #ฟังก์ชันของ Tuple ที่สามารถเรียกใช้ได้ คือ index() และ count()
    A = (1,2,3,3,3,4,5,5,5,6,7,8,8,9)
    print(A.index(4)) # หาตำแหน่งของเลข 4 ที่เจอครั้งแรก คือ index 5
    print(A.count(3)) # นับค่าซ้ำกัน นับค่า 3 ใน tuple
    print(A.count(0)) # นับค่า 0 ใน tuple
    # print(A.index(0)) 0 จะไม่มีใน tuple จะขึ้น error

    print("\n===23===")  #################################################################
    # def read_scores():
    #     scores = ()
    #     done = True
    #     count = 1
    #     while done:
    #         score = int(input(f"enter score #{count} ( -1 to exit) : "))
    #         if score >= 0 and score <= 100:
    #             scores += (score,)
    #             count += 1
    #         elif score == -1:
    #             break
    #     count -= 1
    #     return(scores)
    #
    # def check_grades(scores):
    #     grades = ()
    #     for score in scores:
    #         grade = ""
    #         if score >= 80 :grade = "A"
    #         elif score >= 70: grade = "B"
    #         elif score >= 60: grade = "C"
    #         elif score >= 50: grade = "D"
    #         else: grade = "F"
    #         grades += (grade,)
    #     return grades
    #
    # def report_grades(scores, grades):
    #     Max = len(scores)
    #     print("=" * 24)
    #     print("| No. | Scores | Grade |")
    #     print("=" * 24)
    #     for n in range(Max):
    #         print(f"| %2d  |   %3d  |   %s   |"% (n,scores[n],grades[n]))
    #     print("=" * 24)
    #
    # scores = read_scores()
    # grades = check_grades(scores)
    # report_grades(scores,grades)
    # print(f"End Program.")

    # #ทำแบบง่าย 1
    # count = 1
    # total = 0
    # grade = ""
    # grades = ()
    # scores = ()
    # while True:
    #     score = int(input(f"Enter score {count} ( -1 to exit) : "))
    #     if score == -1:
    #         break
    #     elif score >= 80: grade = "A"
    #     elif score >= 70: grade = "B"
    #     elif score >= 60: grade = "C"
    #     elif score >= 50: grade = "D"
    #     else: grade = "F"
    #     scores += (score,)
    #     grades += (grade,)
    #     count += 1
    #
    # print("=" * 24)
    # print("| No. | Scores | Grade |")
    # print("=" * 24)
    # for i in range(len(grades)):
    #     print(f"|  {i}  |   {scores[i]}   |   {grades[i]}   |")
    # print("=" * 24)
    # print("End Program.")

    # #ทำแบบง่าย 2
    # def read_score():
    #     count = 1
    #     scores = ()
    #     while True:
    #         score = int(input(f"Enter score #{count} ( -1 to exit) : "))
    #         if score >= 0 and score <= 100:
    #             scores += (score,)
    #             count += 1
    #         elif score == -1:
    #             break
    #     return scores
    #
    # def check_grade(scores):
    #     grades = ()
    #     for i in scores:
    #         if i >= 80: grade = "A"
    #         elif i >= 70: grade = "B"
    #         elif i >= 60: grade = "C"
    #         elif i >= 50: grade = "D"
    #         else: grade ="F"
    #         grades += (grade, )
    #     return grades
    #
    # def report_grade(scores,grades):
    #     print("=" * 24)
    #     print("| No. | Scores | Grade |")
    #     print("=" * 24)
    #     for i in range(len(scores)):
    #         print(f"|  {i}  |    {scores[i]}  |   {grades[i]}   |")
    #     print("=" * 24)
    #     print("End Program.")
    #
    # scores = read_score()
    # grades = check_grade(scores)
    # report_grade(scores,grades)

    # ทำแบบง่าย 3
    # def read_score():
    #     count = 1
    #     scores = ()
    #     while True:
    #         score = int(input(f"Enter score #{count} ( -1 to exit) : "))
    #         if score >= 0 and score <= 100:
    #             scores += (score,)
    #             count += 1
    #         elif score == -1:
    #             break
    #     return scores
    #
    # def check_grade(scores):
    #     grades = ()
    #     for i in scores:
    #         if i >= 80: grade = "A"
    #         elif i >= 70: grade = "B"
    #         elif i >= 60: grade = "C"
    #         elif i >= 50: grade = "D"
    #         else: grade = "F"
    #         grades += (grade,)
    #     return grades
    #
    # def report_grade(scores,grades):
    #     print("=" * 24)
    #     print("| No. | Scores | Grade |")
    #     print("=" * 24)
    #     for i in range(len(scores)):
    #         print(f"|  {i}  |    {scores[i]}  |   {grades[i]}   |")
    #     print("=" * 24)
    #     print("End Program.")
    #
    # scores = read_score()
    # greads = check_grade(scores)
    # report_grade(scores, greads)

    #เอาไว้ show ใน terminal
    def read_score():
        count = 0
        score = (89, 45, 55, 66, 77, 88, 52, 68, -1)
        scores = ()
        while True:
            print(f"Enter score #{count+1} ( -1 to exit) : {score[count]}")
            if score[count] >= 0 and score[count] <= 100:
                scores += (score[count],)
                count += 1
            elif score[count] == -1:
                break
        return scores

    def check_grade(scores):
        grades = ()
        for i in scores:
            if i >= 80: grade = "A"
            elif i >= 70: grade = "B"
            elif i >= 60: grade = "C"
            elif i >= 50: grade = "D"
            else: grade = "F"
            grades += (grade,)
        return grades

    def report_grade(scores,grades):
        print("=" * 24)
        print("| No. | Scores | Grade |")
        print("=" * 24)
        for i in range(len(scores)):
            print(f"|  {i}  |    {scores[i]}  |   {grades[i]}   |")
        print("=" * 24)
        print("End Program.")

    scores = read_score()
    greads = check_grade(scores)
    report_grade(scores, greads)

    print("\n===28===")  #################################################################
    # การสร้างลิสต์(List)
    #
    # สมาชิกในลิสต์
    # อาจเป็นข้อมูลชนิดเดียวกันหรือคนละชนิดก็ได้
    #
    # สำหรับการกำหนดค่า
    # สมาชิกของลิสต์
    # วิธีที่ง่ายและสะดวกที่สุด
    # คือ ใช้เครื่องหมายวงเล็บเหลี่ยม[]
    # หรือใช้ฟังก์ชัน
    # list()
    A = [] # empty list
    B = [0, 1, 2]
    C = list([10, 20, 30])
    D = [5]
    E = ["Somchai", "IT", 20, 3.00]
    print(A)
    print(B)
    print(C)
    print(D)
    print(E)

    print("\n===29===")  #################################################################
    Num = [1, 3, 5, 7, 9]
    for i in range(5):
        print(Num[i])

    Colors = ["red", "green", "blue"]
    for c in Colors:
        print(c)

    print("\n===30===")  #################################################################
    # def check_grade(grade):
    #     grades = ["A","B+","B","C+","C","D+","D","F"]
    #     values = [4, 3.5, 3, 2.5, 2, 1.5, 1, 0]
    #     for n in range(len(grades)):
    #         if grade == grades[n]:
    #             return(values[n])
    #         else: pass
    #
    # while True:
    #     grade = input("Enter grade (Q-exit): ").upper()
    #     if grade == "Q":
    #         break
    #     else:
    #         value = check_grade(grade)
    #         print(f"Score value of {grade} is {value}")
    # print("End Program.")

    #ทำแบบง่าย
    # def check_grade(grade):
    #     grades = ["A","B+","B","C+","C","D+","D","F"]
    #     scores = [4,3.5,3,2.5,2,1.5,1,0]
    #     for i in range(len(grades)):
    #         if grade == grades[i]:
    #             return scores[i]
    #         else: pass
    #
    # while True:
    #     grade = input("Enter grade (Q-exit): ").upper()
    #     if grade == "Q":
    #         print("End Program.")
    #         break
    #     print(f"Score value of {grade} is {check_grade(grade)}")

    # ทำไว้ show ใน terminal
    def check_grade(grade):
        grades = ["A","B+","B","C+","C","D+","D","F"]
        values = [4, 3.5, 3, 2.5, 2, 1.5, 1, 0]
        for n in range(len(grades)):
            if grade == grades[n]:
                return(values[n])
            else: pass

    count = 0
    while True:
        grade = ["A","c","d","B","B+","d+","F","C","q"]
        grade = grade[count].upper()
        print(f"Enter grade (Q-exit): {grade}")
        if grade == "Q":
            break
        else:
            value = check_grade(grade)
            print(f"Score value of {grade} is {value}")
        count += 1
    print("End Program.")

    print("\n===32===")  #################################################################
    # การใช้โอเปอเรเตอร์และฟังก์ชันร่วมกับลิสต์
    # โอเปอเรเตอร์(Operators)
    # ที่สามารถใช้ร่วมกับลิสต์
    # +: รวมลิสต์
    # +=: เพิ่มสมาชิกเข้าลิสต์(คล้าย append)
    # *: ทำซ้ำลิสต์
    # in: ตรวจสอบว่าสมาชิกอยู่ในลิสต์หรือไม่
    # not in: ตรวจสอบว่าสมาชิกไม่อยู่ในลิสต์
    # ==: ตรวจสอบว่าลิสต์สองอันเท่ากันหรือไม่
    # !=: ตรวจสอบว่าลิสต์สองอันไม่เท่ากัน

    A = [1, 3]
    B = [2, 4]
    C = A + B
    print(C)
    C += [5,6,7,8] # +=: เพิ่มสมาชิกเข้าลิสต์(คล้าย append)
    print(C)

    if 3 in C: # ถ้ามี 3 ใน c
        print("3 in List C" )

    if 0 not in C: # ถ้ามี 0 ไม่อยู่ใน c
        print("0 not in List C")

    print("\n===33===")  #################################################################
    # def check_rate(total):
    #     rates = [0.10, 0.075, 0.05, 0.025, 0.0]
    #     total_sales = [20000.0, 10000.0, 5000.0, 1000, 1.0]
    #     for n in range(len(total_sales)):
    #         if total > total_sales[n]:
    #             return(rates[n])
    #
    # def get_sale():
    #     sales = []
    #     count = 1
    #     while True:
    #         sale = float(input(f"Enter sale {count} (-1 to exit): "))
    #         if sale > -1.0:
    #             sales += [sale]
    #             count += 1
    #         elif sale == -1.0:
    #             break
    #     return sales
    #
    # sales = get_sale()
    # total = sum(sales)
    # rate = check_rate(total)
    # commission = total * rate
    #
    # print(f"Total sales : {total:.2f}")
    # print(f"Commission Rate : {rate * 100:.2f}%")
    # print(f"Total Commission : {commission:.2f}")

    #แบบง่าย 1
    # def check_rate(total):
    #     rates = [0.10, 0.075, 0.05, 0.025, 0]
    #     total_sale = [20000, 10000, 5000, 1000, 1]
    #     for i in range(len(rates)):
    #         if total > total_sale[i]:
    #             return rates[i]
    #
    # def get_sale2():
    #     sales = []
    #     count = 1
    #     while True:
    #         sale = int(input(f"Enter sale {count} ( -1 to exit): "))
    #         if sale == -1:
    #             break
    #         else:sales += [sale]
    #         count += 1
    #     return sales
    #
    # sales = get_sale2()
    # total = sum(sales)
    # rate = check_rate(total)
    # print(f"Total sales : {total:.2f}")
    # print(f"Commission Rate: {rate * 100:.2f}%")
    # print(f"Total Commission : {total * rate:.2f}")

    # ทำไว้ show ใน terminal
    def check_rate(total):
        rates = [0.10, 0.075, 0.05, 0.025, 0]
        total_sale = [20000, 10000, 5000, 1000, 1]
        for i in range(len(rates)):
            if total > total_sale[i]:
                return rates[i]

    def get_sale2():
        sales = []
        count = 0
        sale = [200, 400, 600, 100, 500, 300, 800, -1]
        while True:
            print(f"Enter sale {count+1} ( -1 to exit): {sale[count]}")
            if sale[count] == -1:
                break
            else:sales += [sale[count]]
            count += 1
        return sales

    sales = get_sale2()
    total = sum(sales)
    rate = check_rate(total)
    print(f"Total sales : {total:.2f}")
    print(f"Commission Rate: {rate * 100:.2f}%")
    print(f"Total Commission : {total * rate:.2f}")

    print("\n===36===")  #################################################################
    # ฟังก์ชันของลิสต์ที่เรียกใช้ได้มีดังนี้:
    # append() count() extend() index() insert() pop() remove() reverse() sort()

    # append(x): เพิ่มค่า x ไปต่อท้ายลิสต์
    # insert(i, x): แทรกค่า x ที่ตำแหน่ง i
    # extend(iterable): เพิ่มสมาชิกจาก iterable (เช่น list หรือ tuple) ต่อท้ายลิสต์
    # index(x): คืนค่าตำแหน่งของ x (ตัวแรกที่พบ) ในลิสต์
    # count(x): นับจำนวนครั้งที่ x ปรากฏในลิสต์
    # remove(x): ลบสมาชิกตัวแรกที่ตรงกับ x ออกจากลิสต์
    # pop([i]): ลบและคืนค่าสมาชิกที่ตำแหน่ง i (หรือลบตัวสุดท้ายของลิสต์โดยอัตโนมัติ) ตัวที่.pop จะย้ายลบค่าที่ list เดิม และย้ายค่ามาที่ .pop แทน
    # sort(): เรียงลำดับสมาชิกในลิสต์ (จากน้อยไปมาก)
    # reverse(): กลับลำดับสมาชิกในลิสต์

    A = [1, 3, 5, 7, 9, 11, 13]
    print(A) # เพิ่ม 13 ต่อท้าย list
    A.insert(2, 6)  # insert(i, x): ที่ตำแหน่ง i แทรกค่า x
    print(A)  # ที่ index 2 แทรกค่า 6
    A.remove(6)# remove(x): ลบสมาชิกตัวแรกที่ตรงกับ x ออกจากลิสต์
    print(A) # ลบค่า 6 ใน list
    print(A.pop())#ค่าตัวสุดท้ายใน list อยู่นี่แทน  # pop([i]): ลบและคืนค่าสมาชิกที่ตำแหน่ง i (หรือลบตัวสุดท้ายของลิสต์โดยอัตโนมัติ) ตัวที่.pop จะย้ายลบค่าที่ list เดิม และย้ายค่ามาที่ .pop แทน
    print(A) #ลบค่าตัวสุดท้ายออก และย้ายค่าไปอยู่ที่ pop เช่น B = a.pop ค่าจะอยู่ที่ B
    print(A.index(7))#หาตำแหน่ง index  # index(x): คืนค่าตำแหน่งของ x (ตัวแรกที่พบ) ในลิสต์
    A.extend([13,15,17]) # extend(iterable(ใส่ค่าได้หลายค่า)): เพิ่มสมาชิกจาก iterable(ใส่ค่าได้หลายค่า) (เช่น list หรือ tuple) ต่อท้ายลิสต์
    print(A) # เพิ่มค่า 13 15 17ต่อท้าย list
    A.reverse() # reverse(): กลับลำดับสมาชิกในลิสต์
    print(A) # reverse(): กลับลำดับสมาชิกในลิสต์
    A.sort() # sort(): เรียงลำดับสมาชิกในลิสต์ (จากน้อยไปมาก)
    print(A) # เรียงจากน้อยไปมาก

    print("\n===37===")  #################################################################
    # from random import randint
    #
    # def read_scores(num):
    #     scores = []
    #     for i in range(num):
    #         scores.append(randint(40,100))
    #     return scores
    #
    # def check_grades(scores):
    #     SCORES = [80, 70, 60, 50, 0]
    #     GRADES = ["A","B","C","D","F"]
    #     grades = []
    #     for score in scores:
    #         for n in range(len(SCORES)):
    #             if score >= SCORES[n]:
    #                 grades.append(GRADES[n])
    #                 break
    #     return(grades)
    #
    # def report_grades(scores, grades):
    #     Max = len(scores)
    #     print("=" * 24)
    #     print("| No. | Scores | Grade |")
    #     print("=" * 24)
    #     for n in range(Max):
    #         print(f"| %2d |   %3d  |  %s  |"%(n+1,scores[n],grades[n]))
    #     print("=" * 24)
    #
    # num = int(input("Enter number student : "))
    # scores = read_scores(num)
    # grades = check_grades(scores)
    # report_grades(scores,grades)
    # print(f"End Program.")

    # # ทำแบบง่าย
    # from random import randint
    # num = int(input("Enter number student : "))
    # print("=" * 24)
    # print("| No. | Scores | Grade |")
    # print("=" * 24)
    # for i in range(1,num+1):
    #     score = randint(40, 100)
    #     if score >= 80: grade = "A"
    #     elif score >= 70: grade = "B"
    #     elif score >= 60: grade = "C"
    #     elif score >= 50: grade = "D"
    #     else: grade = "F"
    #     print(f"| {i:2}  |    {score}  |   {grade}   |")
    # print("=" * 24)
    # print("End Program.")

    # ทำซ้ำ 1
    # from random import  randint
    # def read_scores(num):
    #     scores = []
    #     for i in range(num):
    #         scores.append(randint(40,100))
    #     return scores
    #
    # def check_grades(scores):
    #     score = [80,70,60,50,0]
    #     grades = ["A","B","C","D","F"]
    #     grade = []
    #     for i in scores:
    #         for n in range(len(score)):
    #             if i >= score[n]:
    #                 grade.append(greads[n])
    #     return grade
    #
    # def report_grades(scores,grade):
    #     print("=" * 24)
    #     print("| No. | Scores | Grade |")
    #     print("=" * 24)
    #     for i in range(0,len(scores)):
    #         print(f"| {i+1:2}  |    {scores[i]}  |   {grade[i]}   |")
    #     print("=" * 24)
    #     print("End Program.")
    #
    # num = int(input("Enter number student : "))
    # scores = read_scores(num)
    # grade = check_grades(scores)
    # report_grades(scores,grade)

    # ทำซ้ำ 2
    # from random import randint
    # def read_scores(num):
    #     scores = []
    #     for i in range(num):
    #         score = randint(40,100)
    #         scores.append(score)
    #     return scores
    #
    # def check_grades(scores):
    #     score = [80,70,60,50,0]
    #     grade = ["A","B","C","D","F"]
    #     grades = []
    #     for i in scores:
    #         for n in range(len(score)):
    #             if i >= score[n]:
    #                 grades.append(grade[n])
    #     return grades
    #
    # def report_grades(scores,grades):
    #     print("=" * 24)
    #     print("| No. | Scores | Grade |")
    #     print("=" * 24)
    #     for i in range(0,len(scores)):
    #         print(f"| {i+1:2}  |   {scores[i]:3}  |   {grades[i]}   |")
    #     print("=" * 24)
    #     print("End Program.")
    #
    # num = int(input("Enter number student : "))
    # scores = read_scores(num)
    # grades = check_grades(scores)
    # report_grades(scores, grades)
    # read_scores(num)

    #ทำไว้ show ใน terminal
    from random import randint
    def read_scores(num):
        scores = []
        for i in range(num):
            score = randint(40, 100)
            scores.append(score)
        return scores

    def check_grades(scores):
        score = [80, 70, 60, 50, 0]
        grade = ["A", "B", "C", "D", "F"]
        grades = []
        for i in scores:
            for n in range(len(score)):
                if i >= score[n]:
                    grades.append(grade[n])
        return grades

    def report_grades(scores, grades):
        print("=" * 24)
        print("| No. | Scores | Grade |")
        print("=" * 24)
        for i in range(0, len(scores)):
            print(f"| {i + 1:2}  |   {scores[i]:3}  |   {grades[i]}   |")
        print("=" * 24)
        print("End Program.")

    num = 10
    print(f"Enter number student : {num}")
    scores = read_scores(num)
    grades = check_grades(scores)
    report_grades(scores, grades)
    read_scores(num)

    print("\n===40===")  #################################################################
    #การสร้างลิสต์แบบ 2 มิติ สามารถกำหนดค่าไปเลย หรือแบบค่อยๆสร้างก็ได้
    # A = [[1,2,3],[4,5,6]]
    # for r in range(len(A)): # 0, 1
    #     for c in range(len(A[0])):  # 0, 1, 2
    #         print(A[r][c])
    #
    # # B = []
    # # for r in range(3): # 0, 1, 2
    # #     B.append([])
    # #     for c in range(4): # 0, 1, 2, 3
    # #         B[r].append(c)
    # # print(B)
    # B = []
    # for i in range(3): # 0, 1, 2
    #     B.append([])
    #     for n in range(4): # 0, 1, 2, 3
    #         B[i].append(n) #B[0].append(0,1,2,3)
    # print(B)

    A = [[1,2,3],[4,5,6]]
    for i in range(len(A)):
        for n in range(len(A[i])):
            print(A[i][n])

    B = []
    for i in range(3):
        B.append([])
        for n in range(4):
            B[i].append(n)
    print(B)

    print("\n===41===")  #################################################################
    # from random import randint
    #
    # # main program
    # student = int(input("Enter number of student : "))
    # subject = int(input("enter number of subject : "))
    #
    # #creat list variable
    # scores = []
    # #generate data in list
    # for r in range(student):
    #     scores.append([])
    #     for c in range(subject):
    #         scores[r].append(randint(0,100)) # random value
    #
    # #display
    # for score in scores:
    #     print(score)

    # #ทำแบบง่าย
    # from random import randint
    # std = int(input("Enter number of student : "))
    # sbj = int(input("Enter number of subject : "))
    # A = []
    # for i in range(std):
    #     A.append([])
    #     for n in range(sbj):
    #         A[i].append(randint(0,100))
    # for i in A:
    #     print(i)

    # ทำซ้ำ
    # from random import randint
    # student = int(input("Enter number of student : "))
    # subject = int(input("Enter number of subject : "))
    # scores = []
    # for r in range(student): # 0,1,2,3,4,5,6,7,8,9,10
    #     scores.append([])
    #     for c in range(subject): # 1,2,3,4
    #         scores[r].append(randint(0,100))
    # for score in scores:
    #     print(score)

    # ทำไว้ show ใน terminal
    from random import randint
    student = 10
    subject = 4
    print(f"Enter number of student : {student}")
    print(f"Enter number of subject : {subject}")
    scores = []
    for r in range(student): # 0,1,2,3,4,5,6,7,8,9,10
        scores.append([])
        for c in range(subject): # 1,2,3,4
            scores[r].append(randint(0,100))
    for score in scores:
        print(score)

    print("\n===43===")  #################################################################
    # from random import randint
    #
    # def genData(std, sub):
    #     scores = []
    #     for r in range(std):
    #         scores.append([]) # add list
    #         for c in range(sub):
    #             scores[r].append(randint(0,100))
    #     return scores
    #
    # def reportData(scores):
    #     col = 6 * subject + 5
    #     line = "-" * col
    #     head = "|No.|"
    #     for n in range(1,subject + 1): head += f"Sub{n:2}|"
    #     mess = ""
    #     n = 1
    #     for score in scores:
    #         mess += f"|{n:2} |"
    #         for s in score:
    #             mess += f" {s:3} |"
    #         mess += "\n"
    #         n += 1
    #     print(line, head, line, sep="\n")
    #     print(mess, end = "")
    #     print(line)
    #
    # # main program
    # student = int(input("Enter number of student : "))
    # subject = int(input("enter number of subject : "))
    # # create list variable
    # Scores = genData(student, subject)
    # # generate data in list
    # reportData(Scores)

    #เปิด def เขียนตาม 2
    # from random import randint
    #
    # def genData(std, sub): # 12, 6
    #     scores = [] #สร้าง list
    #     for r in range(std): # 0,1,2,3,4,5,6,7,8,9,10,11
    #         scores.append([]) #[[],[] สร้าเป็น 2 มิติ มี 11 list ]
    #         for c in range(sub): # 0,1,2,3,4,5
    #             scores[r].append(randint(0,100)) #score[r]กำหนดindex listในมิติที่2 [[],[]] และเพิ่มค่าสุ่มในlistมิติที่2 จำนวน 6 ค่า
    #     return scores
    #
    # def reportData(scores):
    #     col = 6 * sub + 5 # sub ละ 6 ช่อง no มี 5 คูณช่องๅ sub เก็บค่าเป็นตัวเลขก่อนไปคูร line บวก str กับ int ไม่ได้แต่ คูณได้
    #     line = "-" * col
    #     head = "|No.|"
    #     for n in range(1,sub+1): head += f"Sub{n:2}|" #ทำ sub loop 1 ถึง sub
    #     mess = "" # สร้างตัวแปรเก็บ str report ทั้งหมด
    #     n = 1 #สร้างแถว เป็นการสร้างแถวโดยยังไม่ใช้ for loop เพราะจะเปิด for loop แบบไม่ต้องกำหนด index ของ list ด้านใน loop
    #     for score in scores: #กำหนดindex list มิติที่ 2 กำหนด score ใน scores(list data random)
    #         mess += f"|{n:2} |" # เก็บข้อความไว้ในตัวแปร mess
    #         for s in score: #กำหนดindex list มิติที่ 1 กำหนด s ใน score คือ index list มิติที่1(ข้อมูลในมิติที่2)
    #             mess += f" {s:3} |" # เก็บข้อความไว้ในตัวแปร mess
    #         mess += "\n" # เมื่อวน index list มิติที่ 1 ครบ ขึ้นบรรทัดใหม่
    #         n += 1 #ื เพิ่มค่า n เมื่อวน index list มิติที่ 1 ครบ
    #     print(line,head,line,sep = "\n") # print line head line เมื่อมีช่องว่างให้เว้นบรรทัด
    #     print(mess,end="") # print mess ที่เก็บไว้แล้วกำหนดการเว้นบรรทัดเป็นว่างเปล้า
    #     print(line) # ขีดด้านล่าง
    #
    # std = int(input("Enter number of student : "))
    # sub = int(input("Enter number of subject : "))
    # scores = genData(std, sub)
    # reportData(scores)

    ##def 1
    # from random import randint
    # def genData(std, sub):
    #     scores = []
    #     for i in range(std):
    #         scores.append([])
    #         for r in range(sub):
    #             scores[i].append(randint(0,100))
    #     return scores
    #
    # def reportData(scores):
    #     head = "|No.|"
    #     mess = ""
    #     for n in range(1,sub+1): head += f"Sub{n:2}|"
    #     line = "-" * len(head)
    #     n = 1
    #     for i in scores: #2
    #         mess += f"|{n:2} |"
    #         for r in i: #1
    #             mess += f" {r:3} |"
    #         mess += "\n"
    #         n += 1
    #     print(line,head,line,sep="\n")
    #     print(mess,end="")
    #     print(line)
    #
    # std = int(input("Enter number of student : "))
    # sub = int(input("Enter number of subject : "))
    # scores = genData(std, sub)
    # reportData(scores)

    #def 2 writeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    # from random import randint
    # def genData(std, sub):
    #     scores = []
    #     for i in range(std):
    #         scores.append([])
    #         for r in range(sub):
    #             scores[i].append(randint(0,100))
    #     return scores
    #
    # def reportData(scores):
    #     head = "|No.|"
    #     for n in range(1,sub+1): head += f"Sub{n:2}|"
    #     line = "-" * len(head)
    #     mess = ""
    #     n = 1
    #     for i in scores:# มิติที่ 1 [45,12,31,78],[12,45,78,45],[78,67,45,21],[32,72,19,74],[98,15,64,78]
    #         mess += f"|{n:2} |"
    #         for r in i: # มิติที่ 2  # 45,12,31,78
    #             mess += f" {r:3} |"
    #         mess += "\n"
    #         n += 1
    #     print(line,head,line,sep="\n")
    #     print(mess,end="")
    #     print(line)
    #
    # std = int(input("Enter number of student : "))
    # sub = int(input("Enter number of subject : "))
    # scores = genData(std, sub)
    # reportData(scores)

    # # list แบบง่าย
    # from random import randint
    # std = int(input("Enter number of student : "))
    # sbj = int(input("Enter number of subject : "))
    # p = "-"
    # sub = "|No.|"
    # random = []
    # for r in range(std):
    #     random.append([])
    #     for rn in range(sbj):
    #         random[r].append(randint(0,100))
    #
    # for i in range(sbj):
    #     sub += f"Sub{i+1:2}|"
    # print(f"{p * len(sub)}\n" + sub + f"\n{p * len(sub)}")
    #
    # for n in range(std):
    #     print(f"|{n+1:2} |",end="")
    #     for n2 in range(sbj):
    #         print(f" {random[n][n2]:3} |",end="")
    #     print()
    # print(f"{p * len(sub)}")

    # ทำแบบง่าย 1
    # from random import randint
    # std = int(input("Enter number of student : "))
    # sbj = int(input("Enter number of subject : "))
    # sub = "|No.|"
    # d = "-"
    # for i in range(sbj):
    #     sub += f"Sub{i+1:2}|"
    # d = d * len(sub)
    # print(d)
    # print(sub)
    # # print(len(sub))
    # print(d)
    # for i in range(std):
    #     print(f"|{i+1:2} |",end="")
    #     for n in range(sbj):
    #         print(f" {randint(0,100):3} |",end="")
    #     print()
    # print(d)

    # # ทำแบบ ง่าย 2
    # from random import randint
    # std = int(input("Enter number of student : "))
    # sbj = int(input("enter number of subject : "))
    # p = "|No.|"
    # for i in range(sbj):
    #     p += f"Sub{i+1:2}|"
    # print("-" * len(p) + f"\n{p}\n" + "-" * len(p))
    # for i in range(std):
    #     print(f"|{i+1:2} |",end="")
    #     for n in range(sbj):
    #         print(f" {randint(0,100):3} |",end="")
    #     print()
    # print("-" * len(p))

    # ทำไว้ show ใน terminal
    from random import randint
    std = 12
    sbj = 6
    print(f"Enter number of student : {std}")
    print(f"Enter number of subject : {sbj}")
    p = "|No.|"
    for i in range(sbj):
        p += f"Sub{i + 1:2}|"
    print("-" * len(p) + f"\n{p}\n" + "-" * len(p))
    for i in range(std):
        print(f"|{i + 1:2} |", end="")
        for n in range(sbj):
            print(f" {randint(0, 100):3} |", end="")
        print()
    print("-" * len(p))


s()