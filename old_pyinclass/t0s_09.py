from random import randint


def s ():
    # ดิกชันนารี (Dictionary)
    # ดิกชันนารี คือ ตัวแปรข้อมูลคอลเลกชัน (Collection) แบบหนึ่งในภาษา Python ที่สามารถเก็บข้อมูลได้หลายค่าในรูปแบบของ “ลำดับรายการ” ด้วยตัวแปรเดียว คล้ายกับลิสต์ (List) แต่จะแตกต่างตรงที่ ค่าของสมาชิกในดิกชันนารีจะประกอบด้วยสองส่วน คือ คีย์ (Key) และแวลู (Value) เราใช้คีย์เพื่อค้นหารายละเอียดหรือข้อมูลของแวลูนั้น ๆ จึงเรียกว่า คีย์-แวลู (Key-Value)
    #
    # คุณลักษณะสำคัญของดิกชันนารี:
    # กำหนดค่าของสมาชิกด้วยเครื่องหมายปีกกา {}
    # โดยแต่ละสมาชิกจะประกอบด้วยคีย์และแวลูในรูปแบบ key: value และคั่นแต่ละสมาชิกด้วยเครื่องหมาย ,
    # student = {"name": "Anna", "age": 20, "grade": "A"}

    # สามารถแก้ไขหรือเปลี่ยนแปลงค่าของสมาชิกได้
    # student["age"] = 21

    # สามารถลบสมาชิกออกได้
    # del student["grade"]
    # นิยมใช้ในกรณีที่มีข้อมูลจำนวนมาก และต้องการเข้าถึงข้อมูลได้รวดเร็วด้วยคีย์

    print("===4===") #########################################################################################################
    # การสร้างและกำหนดค่าดิกชันนารี (Dictionary)
    # ในการสร้างดิกชันนารี เราสามารถกำหนดสมาชิกได้โดยใช้ คีย์ (Key) และ แวลู (Value) ซึ่งอาจเป็นข้อมูลชนิดเดียวกันหรือต่างชนิดกันก็ได้
    #
    # สมาชิกแต่ละคู่จะประกอบด้วย คีย์ : แวลู และคั่นแต่ละคู่ด้วยเครื่องหมาย , โดยรวมอยู่ภายในเครื่องหมายปีกกา {}
    # dictionary_object [key] = value

    A = {}  #Emptry Dictionary
    print(A)

    B = {'1':'one'}
    print(B)

    A[1] = 1500.5 # เพิ่ม key 1 vlaue 1500.5
    print(A)

    B[1] = "Somchai" # เพิ่ม key 1 vlaue "Somchai"
    print(B)

    #C["one"] = 2000 # Error, C not defne

    A[2] = ["Somchai","Cheingpongpan"] # เพิ่ม key 2 value ["somchai","Cheingpongpan"]
    print(A)

    B["B+"] = 3.5 # เพิ่ม key B+ value 3.5
    print(B)

    print("\n===5===") #########################################################################################################
    # การเข้าถึงสมาชิกของดิกชันนารี (Dictionary)
    # ในการ กำหนดข้อมูลสมาชิก ของดิกชันนารี เราจะใช้เครื่องหมายปีกกา {} เพื่อสร้างข้อมูลในรูปแบบ คีย์:แวลู (Key:Value)
    #
    # แต่เมื่อต้องการ เข้าถึง (เรียกใช้) ค่าของสมาชิกในดิกชันนารีแต่ละตัว จะต้องใช้เครื่องหมาย วงเล็บเหลี่ยม [] โดยระบุชื่อ คีย์ (Key) ที่ต้องการเรียกข้อมูล
    #
    # เนื่องจากดิกชันนารีจะไม่เก็บข้อมูลตามลำดับหมายเลขเหมือนลิสต์ แต่จะเข้าถึงข้อมูลโดยอิงจากคีย์เท่านั้น

    Numbers = {1:"one",2:"two",3:"Three"}
    print(Numbers[1])

    for n in Numbers:
        print(n)

    for n in Numbers:
        print(n, Numbers[n])

    print("\n===6===") #########################################################################################################
    # datas = {}
    # for n in range(5):
    #     name = input(f"Enter name %d : " % (n+1))
    #     datas[n] = name
    # print(datas)
    #
    # for n in range(len(datas)):
    #     print(f"datas[%d] = %s" % (n, datas[n]))

    # datas = {} #สร้าง dictionary
    # for i in range(5):
    #     name = input(f"Enter name {i+1} :")
    #     datas[i] = name #สร้าง dictionary  datas[kay] = value
    # print(datas) # แสดง dictionary ทั้งหมด
    # for i in range(len(datas)): #วนรอบตาม key ใน datas
    #     print(f"datas[{i}] = {datas[i]}") # แสดง datas[kay] = value

    # ทำไว้ show ใน terminal
    datas = {}
    name = ["Somchai","Python","Workshop","Scp","101"]
    for i in range(5):
        print(f"Enter name {i+1} : {name[i]}")
        datas[i] = name[i]
    print(datas)
    for i in range(len(datas)):
        print(f"datas[{i}] = {datas[i]}")

    print("\n===8===") #########################################################################################################
    # การใช้โอเปอเรเตอร์และฟังก์ชันร่วมกับดิกชันนารี
    # ดิกชันนารีในภาษา Python สามารถใช้งานร่วมกับ โอเปอเรเตอร์ และฟังก์ชันแบบ Built - in ได้
    # เพื่อช่วยในการตรวจสอบและจัดการข้อมูลภายในดิกชันนารี

    # 🔹 โอเปอเรเตอร์ที่ใช้ร่วมกับดิกชันนารี
    # in: ตรวจสอบว่าคีย์มีอยู่ในดิกชันนารีหรือไม่
    # not in: ตรวจสอบว่าคีย์ไม่มีอยู่ในดิกชันนารี
    # ==: เปรียบเทียบว่าดิกชันนารีสองตัวมีค่าคีย์ - แวลูเหมือนกันหรือไม่
    # !=: เปรียบเทียบว่าดิกชันนารีสองตัวมีค่าคีย์ - แวลูต่างกันหรือไม่
    #
    # ฟังก์ชันแบบ
    # Built - in ที่ใช้กับดิกชันนารี
    # len(dictionary): คืนค่าจำนวนสมาชิกในดิกชันนารี
    # max(dictionary): คืนค่าคีย์ที่มีค่าสูงสุด(ตามลำดับอักขระหรือเลข)
    # min(dictionary): คืนค่าคีย์ที่มีค่าต่ำสุด
    # sum(dictionary): ใช้ได้เฉพาะเมื่อ คีย์ หรือ แวลู เป็นตัวเลขเท่านั้น(มักใช้กับ.values())
    A = {}
    if (A == {}):
        print("A is Empty Dictionary")

    B = {"1":"One","2":"Two","3":"Three"}
    if (B != {}):
        print("B isn't Empty dictionary")

    A[1] = "one"
    A[5] = "five"
    if 5 in A: # ถ้ามี 5 ใน A
        print("5 in key member A")

    print(len(A)) #คืนค่าจำนวนสมาชิกในดิกชันนารี
    print(len(B)) #คืนค่าจำนวนสมาชิกในดิกชันนารี
    print(max(A)) #คืนค่าคีย์ที่มีค่าสูงสุด(ตามลำดับอักขระหรือเลข)
    print(min(A)) #คืนค่าคีย์ที่มีค่าต่ำสุด
    print(sum(A)) #ใช้ได้เฉพาะเมื่อ คีย์ หรือ แวลู เป็นตัวเลขเท่านั้น(มักใช้กับ.values())
    print(max(B)) #คืนค่าคีย์ที่มีค่าสูงสุด(ตามลำดับอักขระหรือเลข)
    print(min(B)) #คืนค่าคีย์ที่มีค่าต่ำสุด
    # print(sum(B) Error #ใช้ได้เฉพาะเมื่อ คีย์ หรือ แวลู เป็นตัวเลขเท่านั้น(มักใช้กับ.values())

    print("\n===10===") #########################################################################################################
    # def checkGrade(score):
    #     grades = {80:"A",70:"B",60:"C",50:"D",0:"F"}
    #     for n in grades:
    #         if score >= n:
    #             return (grades[n])
    # done = True
    # while done:
    #     score = int(input("Enter your score (-1 to exit) : "))
    #     if score != -1:
    #         grade = checkGrade(score)
    #         print(f"Your score = %d, got grade = %s"%(score,grade))
    #     else:
    #         done = False
    # print("End Program")

    # #แบบง่าย
    # def checkGrade(score):
    #     grade = {80:"A",70:"B",60:"C",50:"D",0:"F"}
    #     for i in grade:
    #         if score >= i:
    #             return grade[i]
    # while True:
    #     score = int(input("Enter your score (-1 to exit) : "))
    #     if score != -1:
    #         print(f"Your score = {score}, got grade = {checkGrade(score)}")
    #     else:break
    # print("End Program")

    # # ทำไว้ show ใน terminal
    # def checkGrade(score):
    #     grade = {80:"A",70:"B",60:"C",50:"D",0:"F"}
    #     for i in grade:
    #         if score >= i:
    #             return grade[i]
    # count = 0
    # while True:
    #     score = [50,60,70,80,44,55,76,84,-1]
    #     score = score[count]
    #     print(f"Enter your score (-1 to exit) : {score}")
    #     if score != -1:
    #         print(f"Your score = {score}, got grade = {checkGrade(score)}")
    #     else:break
    #     count += 1
    # print("End Program")

    print("\n===12===") #########################################################################################################

    # ฟังก์ชันของดิกชันนารี
    # ฟังก์ชันของดิกชันนารีที่สามารถเรียกใช้ได้ มีดังนี้:
    # get(key, default) – คืนค่าของ key ที่ระบุ หากไม่มีให้คืนค่า default
    # pop(key, default) – ลบคู่ key และ value ที่ระบุ และคืนค่า value นั้น
    # popitem() – ลบและคืนคู่ key-value ล่าสุดที่ถูกเพิ่มเข้ามา
    # items() – คืนค่ารายการของคู่ key-value ทั้งหมดในรูปแบบ tuple
    # keys() – คืนค่ารายการของ key ทั้งหมด
    # values() – คืนค่ารายการของ value ทั้งหมด
    # clear() – ลบข้อมูลทั้งหมดในดิกชันนารี
    # copy() – คืนค่าดิกชันนารีสำเนา (copy)
    # update() – ใช้เพิ่มหรืออัปเดตข้อมูลจากอีกดิกชันนารีหนึ่ง
    print(A)
    print(B)
    print(A.get(3)) # return default none
    print(A.get(4,"not found"))
    print(A.get(5))  # คืนค่าของ key ที่ระบุ หากไม่มีให้คืนค่า default
    print(B.items()) # คืนค่ารายการของคู่ key-value ทั้งหมดในรูปแบบ tuple
    print(A.keys()) # คืนค่ารายการของ key ทั้งหมด
    print(A.items()) # คืนค่ารายการของคู่ key-value ทั้งหมดในรูปแบบ tuple
    print(A.pop(1)) # ลบคู่ key และ value ที่ระบุ และคืนค่า value นั้น
    print(A)
    print(B.popitem()) # ลบและคืนคู่ key-value ล่าสุดที่ถูกเพิ่มเข้ามา
    print(B)
    C = A.copy() # คืนค่าดิกชันนารีสำเนา (copy)
    print(C)
    A.update(B) # ใช้เพิ่มหรืออัปเดตข้อมูลจากอีกดิกชันนารีหนึ่ง
    print(A)
    B.clear() # ลบข้อมูลทั้งหมดในดิกชันนารี
    print(B)

    print("\n===15===") #########################################################################################################
    # from random import randint
    #
    # def randomScores(scores):
    #     for n in range(1, 11):
    #         scores[n] = randint(0,100) # key = value
    #
    # def checkGrade(scores, grades):
    #     GRADES = {80:"A",70:"B",60:"C",50:"D",0:"F"}
    #     for n, score in scores.items(): # คืนค่ารายการของคู่ key-value ทั้งหมดในรูปแบบ tuple
    #         for key, value in GRADES.items(): # คืนค่ารายการของคู่ key-value ทั้งหมดในรูปแบบ tuple
    #             if score >= key:
    #                 grades[n] = value
    #                 break
    #
    # def reportGrade(scores, grades):
    #     print("=" * 23)
    #     print("| No. | Score | Grade |")
    #     print("=" * 23)
    #     for n in scores:
    #         print(f"| %3d |  %3d  |   %s   |"%(n, scores[n], grades[n]))
    #     print("=" * 23)
    #
    # scores = {}
    # grades = {}
    # randomScores(scores)
    # print(scores)
    # checkGrade(scores, grades)
    # print(grades)
    # reportGrade(scores, grades)

    # ทำแบบง่าย 1
    # from random import randint
    # def randomScores(scores):
    #     for i in range(1,11):
    #         scores[i] = randint(0,100)
    #
    # def checkGrade(scores, grades):
    #     GRADE = {80:"A",70:"B",60:"C",50:"D",0:"F"}
    #     for n, score in scores.items(): # คืนค่ารายการของคู่ key-value ทั้งหมดในรูปแบบ tuple
    #         for key, value in GRADE.items(): # คืนค่ารายการของคู่ key-value ทั้งหมดในรูปแบบ tuple
    #             if score >= key:
    #                 grades[n] = value
    #                 break
    # def reportGrade(scores, grades):
    #     print("=" * 23)
    #     print("| No. | Score | Grade |")
    #     print("=" * 23)
    #     for n in scores:
    #         print(f"|  {n:2} |   {scores[n]:2}  |   {grades[n]}   |")
    #     print("=" * 23)
    #
    # scores = {}
    # grades = {}
    # randomScores(scores)
    # checkGrade(scores, grades)
    # print(scores)
    # print(grades)
    # reportGrade(scores, grades)

    # ทำแบบง่าย 2
    # from random import randint
    #
    # def randomScores(scores):
    #     for i in range(1,11):
    #         scores[i] = randint(0,100)
    #
    # def checkGrade(scores, grades):
    #     GRADE = {80:"A",70:"B",60:"C",50:"D",0:"F"}
    #     for n, score in scores.items(): # คืนค่ารายการของคู่ key-value ทั้งหมดในรูปแบบ tuple
    #         for key, value in GRADE.items(): # คืนค่ารายการของคู่ key-value ทั้งหมดในรูปแบบ tuple
    #             if score >= key:
    #                 grades[n] = value
    #                 break # break เพื่อ หยุด การวนลูปหาเกรดเมื่อเกรดที่เหมาะสมแล้ว ถ้าไม่หยุดเกรดจะถูกเขียนทับไปเรื่อยๆ break จะหยุดแค่ loop ที่อยู่ระดับเดียวกัน for อันแรกจะไม่ถูกหยุด
    #
    # def reportGrade(scores, grades):
    #     print("=" * 23,"\n| No. | Score | Grade |\n","=" * 23)
    #     for i in scores:
    #         print(f"| {i:2} |    {scores[i]:2}  |   {grades[i]}   |")
    #     print("=" * 23)
    #
    # scores = {}
    # grades = {}
    # randomScores(scores)
    # checkGrade(scores, grades)
    # reportGrade(scores, grades)

    # # ทำแบบง่าย 3
    from random import randint
    def randomScores(scores):
        for i in range(1,11):
            scores[i] = randint(0,100)

    def checkGrade(scores, grades):
        GRADE = {80:"A",70:"B",60:"C",50:"D",0:"F"}
        for k, v in scores.items(): # ต้องมี items เสมอถ้าต้องการหา key and value
            for key, value in GRADE.items():
                if v >= key:
                    grades[k] = value
                    break

    def reportGrade(scores, grades):
        line = "="
        head = "| No. | Score | Grade |"
        print(line * len(head),head,line * len(head),sep="\n")
        for i in scores:
            print(f"|  {i:2} |  {scores[i]:3}  |   {grades[i]}   |")
        print(line * len(head))
    scores = {}
    grades = {}
    randomScores(scores)
    checkGrade(scores,grades)
    reportGrade(scores, grades)

    print("\n===18===") #########################################################################################################
    # from random import randint
    # def inputSales(Sales):
    #     for n in range(1,5):
    #         key = input("Enter branch name : ")
    #         value = []
    #         for m in range(1,5):
    #             data = float (input(f"Enter sales in Quarter {m} : "))
    #             value.append(data)
    #         Sales[key] = value
    #
    # def calTotalSales(Sales):
    #     for key in Sales:
    #         total = 0
    #         for sale in Sales[key]:
    #             total += sale
    #         Sales[key].append(total)
    #
    # def reportSales(Sales):
    #     head = ("| No. | Branch Name | Quarter1 | Quarter2 | Quarter3 | Quarter4 |   Total  |")
    #     print("=" * len(head), head, "=" * len(head),sep="\n")
    #     n = 1
    #     for key in Sales:
    #         print(f"| %2d  | %11s |"% (n,key),end="")
    #         for sale in Sales[key]:
    #             print(f" %8.2f |"% sale, end="")
    #         print()
    #     print("=" * len(head))
    #
    # Sales = {}
    # inputSales(Sales)
    # calTotalSales(Sales)
    # reportSales(Sales)
    # for key in Sales:
    #     print(key, Sales[key])

    # from random import randint
    #
    # def inputSales(Sales):
    #     for i in range(1,5):
    #         branch = input("Enter branch name : ")
    #         value = []
    #         for n in range(1,5):
    #             Quarter = int(input(f"Enter sales in Quarter {n} : "))
    #             value.append(Quarter)
    #         Sales[branch] = value
    #
    # def calTotalSales(Sales):
    #     for key in Sales:
    #         total = 0
    #         for i in Sales[key]:
    #             total += i
    #         Sales[key].append(total)
    #
    # def reportSales(Sales):
    #     head = "| No. | Branch Name | Quarter1 | Quarter2 | Quarter3 | Quarter4 |   Total  |"
    #     print("=" * len(head), head , "=" * len(head),sep="\n")
    #     n = 1
    #     for key in Sales:
    #         print(f"|  {n}  | {key:>11} |",end="")
    #         for value in Sales[key]:
    #             print(f"{value:9.2f} |",end="")
    #         print()
    #     print("=" * len(head))
    #
    # Sales = {}
    # inputSales(Sales)
    # calTotalSales(Sales)
    # reportSales(Sales)
    # for key in Sales:
    #     print(key,Sales[key])

    #ทำซ้ำ 1
    # # f-string เพิ่มเติม
    # #  > = ชิดขวา (right align)
    # #  < = ชิดซ้าย (default)
    # #  ^ = กึ่งกลาง (center)
    # #  11 = ความกว้าง 11 ช่อง
    # from random import randint
    #
    # def inputSales(Sales):
    #     for i in range(1,5):
    #         branch = input("Enter branch name : ")
    #         value = []
    #         for i in range(1,5):
    #             Quarter = int(input(f"Enter sales in Quarter {i} : "))
    #             value.append(Quarter)
    #         Sales[branch] = value
    #
    # def calTotalSales(Sales):
    #     for key in Sales:
    #         total = 0
    #         for i in Sales[key]:
    #             total += i
    #         Sales[key].append(total)
    #
    # def reportSales(Sales):
    #     head = "| No. | Branch Name | Quarter1 | Quarter2 | Quarter3 | Quarter4 |   Total  |"
    #     print("=" * len(head),head,"=" * len(head),sep="\n")
    #     for key in Sales:
    #         print(f"|  1  | {key:>11} |",end="")
    #         for i in Sales[key]:
    #             print(f"{i:9.2f} |",end="")
    #         print()
    #     print("=" * len(head))
    #     for key in Sales:
    #         print(key,Sales[key])
    #
    # Sales = {}
    # inputSales(Sales)
    # calTotalSales(Sales)
    # reportSales(Sales)


    # #แบบง่าย
    # re = {}
    # for i in range(1,5):
    #     branch = input("Enter branch name : ")
    #     quarters = []
    #     for i in range(1,5):
    #         quarter = float(input(f"Enter sales in Quarter {i} : "))
    #         quarters.append(quarter)
    #     re[branch] = quarters
    # line = "="
    # head = "| No. | Branch Name | Quarter1 | Quarter2 | Quarter3 | Quarter4 |   Total  |"
    # print(line * len(head),head,line * len(head),sep="\n")
    # n = 1
    # for i in re:
    #     print(f"|  {n}  |           {i} |    {re[i][0]:.2f} |    {re[i][1]:.2f} |    {re[i][2]:.2f} |   {re[i][3]:.2f}   |  {sum(re[i]):.2f} |")
    # print(line * len(head))
    # for i in re:
    #     print(i,re[i])

    # ทำไว้ show ใน terminal
    from random import randint

    def inputSales(Sales):
        count = 0
        count2 = 0
        for i in range(1, 5):
            branch = ["A","B","C","D"]
            Quarter = [34, 56, 22, 67, 56, 23, 44, 88, 32, 66, 44, 33, 44, 22, 66, 11]
            print(f"Enter branch name : {branch[i-1]}")
            value = []
            for i in range(1, 5):
                print(f"Enter sales in Quarter {i} : {Quarter[count]}")
                value.append(Quarter[count])
                count += 1
            Sales[branch[count2]] = value
            count2 += 1

    def calTotalSales(Sales):
        for key in Sales:
            total = 0
            for i in Sales[key]:
                total += i
            Sales[key].append(total)

    def reportSales(Sales):
        head = "| No. | Branch Name | Quarter1 | Quarter2 | Quarter3 | Quarter4 |   Total  |"
        print("=" * len(head), head, "=" * len(head), sep="\n")
        for key in Sales:
            print(f"|  1  | {key:>11} |", end="")
            for i in Sales[key]:
                print(f"{i:9.2f} |", end="")
            print()
        print("=" * len(head))
        for key in Sales:
            print(key, Sales[key])

    Sales = {}
    inputSales(Sales)
    calTotalSales(Sales)
    reportSales(Sales)

    print("\n===23===") #################################################################

    # เซต (Set) คือตัวแปรชนิดหนึ่งในภาษา Python ที่ใช้เก็บข้อมูลหลายค่าในตัวแปรเดียวกัน
    # ลักษณะคล้ายกับ ลิสต์ (List) แต่มีคุณสมบัติเฉพาะคือ ไม่สามารถมีสมาชิกซ้ำกันได้ ###################
    # คุณลักษณะสำคัญของเซต:
    # กำหนดค่าด้วยเครื่องหมายวงเล็บปีกกา { }
    # สามารถเพิ่มสมาชิกได้
    # สามารถลบสมาชิกออกได้
    # สมาชิกของเซตจะไม่เรียงลำดับ ถ้าไม่ใช้ for  และไม่มีค่าซ้ำ #############################

    # การสร้างเซตและกำหนดค่า
    # การกำหนดค่าสมาชิกให้กับ เซต (Set) สามารถทำได้ 2 วิธีหลัก ๆ คือ:
    # ใช้เครื่องหมายวงเล็บปีกกา {}
    # ใช้คำสั่ง set()

    A = set()
    B = {3,4,5}
    print(A)
    print(B)
    C = {3, "A", 5, "B"}
    print(C) # สมาชิกของเซตจะไม่เรียงลำดับ
    D = {4,2,2,5,1,2}
    print(D) #สมาชิกของเซตไม่มีค่าซ้ำ

    print("\n===24===") #################################################################
    # การเข้าถึงสมาชิกของซต
    # การอ้างถึงสมาชิกแต่ละตัวในเซต จะต้องใช้การวนลูปด้วย for ไม่ สามารถอ้างอิ้งด้วยหมายเลขลำดับได้
    for i in C: # การอ้างถึงสมาชิกแต่ละตัวในเซต จะต้องใช้การวนลูปด้วย for
        print(i)

    print()

    for i in D: # การอ้างถึงสมาชิกแต่ละตัวในเซต จะต้องใช้การวนลูปด้วย for
        print(i)

    print("\n===25===") #################################################################

    # โอเปอเรเตอร์ที่ใช้ร่วมกับเซต

    # in	ตรวจสอบว่าสมาชิกอยู่ในเซต	    'apple' in fruits
    # not in	ตรวจสอบว่าสมาชิกไม่อยู่ในเซต	'banana' not in fruits
    # ==	เซตสองเซตเท่ากันหรือไม่	    {1,2} == {2,1} → True
    # !=	เซตสองเซตไม่เท่ากันหรือไม่	    {1,2} != {1,2,3} → True

    # ฟังก์ชันแบบ Built-in ที่ใช้กับเซต
    # ฟังก์ชัน	ความหมาย	ตัวอย่าง
    # len(set)	นับจำนวนสมาชิกในเซต	len({1,2,3}) → 3
    # max(set)	หาค่าสูงสุดในเซต	    max({5,8,3}) → 8
    # min(set)	หาค่าต่ำสุดในเซต	    min({5,8,3}) → 3
    # sum(set)	ผลรวมค่าทั้งหมดในเซต	sum({1,2,3}) → 6

    if C == D:
        print("Set C == Set D\n")

    if C != D: #ถ้า set c ไม่เท่ากับ set d
        print("Set C != set D\n")

    if 3 in C:# ถ้า 3 อยู่ใน set C  # in	ตรวจสอบว่าสมาชิกอยู่ในเซต
        print("3 is member in C\n")

    if "C" not in C:#ถ้า C ไม่อยู๋ใน set C   # not in	ตรวจสอบว่าสมาชิกไม่อยู่ในเซต
        print("'c' is not member in C\n")

    print("\n===26===") #################################################################
    print(len(C)) # len(set)	นับจำนวนสมาชิกในเซต
    print(len(D))
    print(max(D)) # max(set)	หาค่าสูงสุดในเซต
    print(min(D)) # min(set)	หาค่าต่ำสุดในเซต
    print(sum(D)) # sum(set)	ผลรวมค่าทั้งหมดในเซต
    # print(max(C)) # error เพราะมีค่า str กับ int หาร่วมกันไม่ได้

    print("\n===27===") #################################################################

    # ฟังก์ชันสำหรับจัดการสมาชิก
    # add(item)	เพิ่มสมาชิกเข้าเซต	s.add(5)
    # update(iterable)	เพิ่มหลายสมาชิกจากข้อมูลที่วนซ้ำได้ เช่น list	s.update([1, 2, 3])
    # remove(item)	ลบสมาชิก ถ้าไม่มีจะเกิดข้อผิดพลาด	s.remove(2)
    # discard(item)	ลบสมาชิก ถ้าไม่มีจะไม่เกิดข้อผิดพลาด ถ้าสมาชิก ไม่มีอยู่ → ไม่เกิดข้อผิดพลาด	s.discard(2)
    # clear()	ลบสมาชิกทั้งหมดในเซต	s.clear()

    # ฟังก์ชันสำหรับจัดการเซตกับเซตอื่น
    # union(other_set)	รวมสมาชิกทั้งสองเซต (ไม่ซ้ำกัน)	a.union(b)
    # intersection(other_set)	สมาชิกที่มีร่วมกันในทั้งสองเซต	a.intersection(b)
    # difference(other_set)	สมาชิกที่อยู่ในเซตแรกแต่ไม่อยู่ในอีกเซต	a.difference(b)
    # symmetric_difference(other_set)	สมาชิกที่ไม่ซ้ำกันใน

    C.add("C")
    print(C) # add(item)	เพิ่มสมาชิกเข้าเซต
    print(D)
    # D.remove(0) error ไม่มีค่าใน set
    D.remove(2) # remove(item)	ลบสมาชิก ถ้าไม่มีจะเกิดข้อผิดพลาด
    print(D)
    D.discard(2)# discard(item)	ลบสมาชิก ถ้าไม่มีจะไม่เกิดข้อผิดพลาด ถ้าสมาชิก ไม่มีอยู่ → ไม่เกิดข้อผิดพลาด
    print(D)
    D.discard(4) # discard(item)	ลบสมาชิก ถ้าไม่มีจะไม่เกิดข้อผิดพลาด
    print(D)
    E = C.union(D)#รวม C กับ D เป็น E # union(other_set)	รวมสมาชิกทั้งสองเซต (ไม่ซ้ำกัน)
    print(E)# รวม set C D
    E = C.intersection(D)# 5 คือค่าที่อยู๋ร่วมกัน 2 set # intersection(other_set)	สมาชิกที่มีร่วมกันในทั้งสองเซต
    print(E)
    E = C.difference(D) # difference(other_set)	สมาชิกที่อยู่ในเซตแรกแต่ไม่อยู่ในอีกเซต
    print(E)# ค่าอยู่ set c แต่ไม่อยู๋ set d
    E = C.symmetric_difference(D) # สมาชิกที่ไม่ซ้ำกันใน
    print(E)#ไม่ซ้ำกับ D

    print("\n===29===") #################################################################
    A = {10,40,"one",22,"two",40,"on","IEEE"}

    print("Set A have member : ", len(A))
    print("Member in Set A : ")
    for i in A: # การอ้างถึงสมาชิกแต่ละตัวในเซต จะต้องใช้การวนลูปด้วย for
        print(i)

    print("\n===30===") #################################################################
    # A = set()
    # menu = " 1. Add Item\n 2. Remove Item\n 3. Display Set\n 4. Exit\nEnter choice : "
    # while True:
    #     choice = int(input(menu))
    #     if choice == 1:
    #         print("Add Item")
    #         data = int(input("Enter number : "))
    #         A.add(data) # add(item)	เพิ่มสมาชิกเข้าเซต
    #     elif choice == 2:
    #         print("Remove Item")
    #         data = int(input("Enter number to remove : "))
    #         A.remove(data) # remove(item)	ลบสมาชิก ถ้าไม่มีจะเกิดข้อผิดพลาด
    #         print()
    #     elif choice == 3:
    #         print(A) # show set data
    #     elif choice == 4:
    #         print("Exit Program") #ออก จบ while
    #         break
    #     else:
    #         print("No choice") # ไม่มี choice

    # ทำซ้ำ 1
    # A = set()
    # menu = " 1. Add Item\n 2. Remove Item\n 3. Display Set\n 4. Exit\nEnter choice : "
    # while True:
    #     choice = int(input(menu))
    #     if choice == 1:
    #         print("Add Item")
    #         data = int(input("Enter number : "))
    #         A.add(data)
    #     elif choice == 2:
    #         print("Remove Data")
    #         data = int(input("Enter number to remove : "))
    #         A.remove(data)
    #         print()
    #     elif choice == 3:
    #         print(A)
    #     elif choice == 4:
    #         print("Exit Program")
    #         break
    #     else:
    #         print("No choice")

    # ทำไว้ show ใน terminal
    # A = set()
    # count = 0
    # c = 0
    # menu = " 1. Add Item\n 2. Remove Item\n 3. Display Set\n 4. Exit\nEnter choice : "
    # while True:
    #     choice = [1,3,1,3,1,3,2,3,5,4]
    #     number = [12,44,66,12,0]
    #     choice = choice[count]
    #     number = number[c]
    #     print(menu,choice,sep="")
    #     if choice == 1:
    #         print("Add Item")
    #         print(f"Enter number : {number}")
    #         A.add(number)
    #         c += 1
    #     elif choice == 2:
    #         print("Remove Data")
    #         print(f"Enter number to remove : {number}")
    #         A.remove(number)
    #         print()
    #         c += 1
    #     elif choice == 3:
    #         print(A)
    #     elif choice == 4:
    #         print("Exit Program")
    #         break
    #     else:
    #         print("No choice")
    #     count += 1
s()

