from numpy.random import choice


def s1():
    print("===3===")
    S1 = "Hello World"
    S2 = "สวัสดี ชาวโลก"
    print(S1, S2)

    print("\n===4===")
    S3 = """    This is first lne
    This is second line
    This is third line"""
    print(S3)

    print("\n===5===")
    S1 = "Python"
    S2 = "Hello World"
    Salary = 15980.00
    Age = 34
    import sys
    print(sys.getsizeof(S1)) #หากจะสตรวจสอบขนาดของหน่วยความจำที่ใช้ไป้ของตัวแปร สามรถใช้ getsizeof()
    print(sys.getsizeof(S2)) # เป็นฟังก์ชันซึ่งอยู่ใน Library sys
    print(sys.getsizeof(""))
    print(sys.getsizeof(Salary))
    print(sys.getsizeof(Age))
    print(sys.getsizeof(0))

    print("\n===6===")
    s1 = "Hello"
    s2 = "Python"
    s3 = "Programming"
    s4 = s1 + " " + s2 + " " + s3
    print(s4)

    print("\n===7===")
    s1 = "python"
    s2 = "Python "
    print(s1 * 3)
    print(3 * s2)
    print("=" * 30)
    print(30 * "=")

    print("\n===8===")
    # name = input("Enter your name : ")
    name = "Paphavin"
    num = 5
    print()
    print(name * num)
    print("Show Triangle")
    print(num * "*")
    print((num - 1) * "*")
    print((num - 2) * "*")
    print((num - 3) * "*")
    print((num - 4) * "*")

    print("\n===11===")
    name = "Somchai"
    print("Length of name = %d" % len(name))
    print("name position 0 = ", name [0])
    print("name position -1 = ", name[-1])
    print("name position 3 = ", name[3])
    print("name position -4 = ", name[-4])

    print("\n===12===")
    name = "Somchai"
    print("name slicing 0:3 = ", name[0:3]) #เป็ฯการระบุตำแหน่งเริ่มต้นและตำแหน่งสุดท้าย
    print("name slicing 3:7 = ", name[3:7]) #รูปแบบ str[start:stop]
    print("name slicing 3: = ", name[3:])
    print("name slicing :4 = ", name[:4])
    print("name slicing -1:-4 = ", name[-1:-4])
    print("name slicing -5:-1 = ", name[-5:-1])
    print("name slicing : = ", name[:])

    print("\n===13===")
    name = "Somchai"
    print("name slicing 0: :2") #เป็นการระบุตำแหน่งเริ่มต้น ตำแหน่งสุดท้าย และการกระโดดข้าม
    print("name slicing 0: :2 = ", name[0: :2]) # 0 ถึงสุดท้าย กำหนด step 2
    print("name slicing 0: :3 = ", name[0: :3]) # 0 ถึงสุดท้าย กำหนด step 3
    print("name slicing -7: :2 = ", name[-7: :2]) # -7 ถึงสุดท้าย กำหนด step 2
    print("name slicing -7: :4 = ", name[-7: :4]) # -7 ถึงสุดท้าย กำหนด step 4

    print("\n===14===")
    # name = input("Enter your name : ")
    name = "Somchai"
    print(f"Enter your name : {name}")
    num = len(name)
    print()
    print("Show Triangle name")
    print(name[:num]) # เริ่มต้น ถึงสุดท้าย
    print(name[:num - 1]) # เริ่มต้น ถึง -1
    print(name[:num - 2]) # เริ่มต้น ถึง -2
    print(name[:num - 3]) # เริ่มต้น ถึง -3
    print(name[:num - 4]) # เริ่มต้น ถึง -4
    print(name[:num - 5]) # เริ่มต้น ถึง -5
    print(name[:num - 6]) # เริ่มต้น ถึง -6

    print("\n===17===")
    print("% ใช้สำหรับจัดรูปแบบและหากต้องการแสดง % ใช้ %%")
    print("%c ใช้สำหรับจัดรูปแบบอักขระ")
    print("%d, %i ใช้สำหรับจัดรูปแบบจำนวนเต็ม")
    print("%f, %F ใช้สำหรับจัดรูปแบบตัวเลขทศนิยม")
    print("%e, %E ใช้สำหรับจัดรูปแบบตัวเลขทศนิยมแบบยกกำลังตัวเล็กและตัวใหญ่")
    print("%g, %G ใช้สำหรับจัดรูปแบบตัวเลขอย่างสั้น(ค่าศูนย์ไม่แสดง)")
    print("%o ใช้สำหรับจัดรูปแบบตัวเลขเป็นฐานแปด")
    print("%s ใช้สำหรับรูปแบบสตริง")
    print("%u ใช้สำหรับจัดรูปแบบตัวเลขจำนวนเต็มแบบไม่คิดเครื่องหมาย")
    print("%x, %X ใช้สำหรับจัดรูปแบบตัวเลขจำนวนเต็มฐานสิบหกแบบตัวเล็กและตัวใหญ่")

    print("\n===18===")
    name = "Python"
    print('%s' % name)
    print("|%s|" % name)
    print("|%10s|" % name)
    print("|%-10s|" % name)
    print("|%-10c|" % name[0])
    print("|%10c|" % name[0])

    print("\n===19===")
    num = 8
    print("|%d|" % num)
    print("|%3d|" % num)
    print("|%-3d|" % num)
    print("|%03d|" % num)
    print("|%-03d|" % num)

    print("\n===20===")
    gpa = 2.9580
    print("|%f|" % gpa)
    print("|%d|" % gpa)
    print("|%.2f|" % gpa)
    print("|%5.2f|" % gpa)
    print("|%7.3f|" % gpa)
    print("|%07.3f" % gpa)

    print("\n===21===")
    # total = 0.0
    # for n in range(1,5):
    #     point = int(input(f"Enter point great {n} (0-4) : "))
    #     total += point
    #
    # credit = 4
    # gpa = total / credit
    # print()
    # print("You have %d subject" % credit)
    # print("You have total point = %5.2f, %d credit" % (total, credit))
    # print("You get gpa = %5.2f" % gpa)

    #ทำไว้ show ใน terminal
    credit = 4
    total = 0
    point = [2, 3, 4, 1]
    for i in range(1,5):
        print(f"Enter point grade {i} (0-4) : {point[i-1]}")
        total += point[i-1]
    gpa = total / credit
    print(f"\nYou have {credit} subject")
    print(f"You have total point = {total:.2f}, {credit} credit")
    print(f"You get gap = {gpa}")

    print("\n===24===")
    name = "Somchai"
    salary = 25200.566
    number = 3500
    print(f"|{name}|{salary}|{number}|")
    print(f"|{name:10}|{salary:12}|{number:8}|")
    print(f"|{name:10}|{salary:12.2f}|{number:8,}|")
    print(f"|{name:10}|{salary:12,}|{number:8,}|")

    print("\n===24===")
    import math
    print("")
    print("=" * 40)
    print("|Angel|   Sin    |   Cos    |   Tan     |")
    print("=" * 40)
    for angle in range(0,361, 20):
        radian = math.radians(angle)
        print(f"|%4d |" % angle,end='')
        print("%9.5f |" % math.sin(radian),end='')
        print("%9.5f |" % math.cos(radian),end='')
        print("%9.5f  |" % math.tan(radian))
    print("=" * 40)

    print("\n===25===")
    # print("=" * 40)
    # print("|Angel|   Sin    |   Cos    |   Tan    |")
    # print("=" * 40)
    # for angle in range(0, 361, 20):
    #     radian = math.radians(angle)
    #     print(f"|{angle:4} |", end = "")
    #     print(f"{math.sin(radian):9.5f} |", end = "")
    #     print(f"{math.cos(radian):9.5f} |", end = "")
    #     print(f"{math.tan(radian):9.5f} |")
    # print("=" * 40)

    print("=" * 40)
    print("|Angle|   Sin    |   Cos    |   Tan    |")
    print("=" * 40)
    for angle in range(0,361,20):
        radian = math.radians(angle)
        print(f"|{angle:4} |{math.sin(radian):9.5f} |{math.cos(radian):9.5f} |{math.tan(radian):9.5f} |")
    print("=" * 40)

    print("\n===31===")
    s = "Python312"
    print(f"Enter string : {s}")
    print()
    print("String is alpha = ", s.isalpha()) #สำหรับตรวจสอบสตริงว่ามีค่าเป็นตัวอักษรเท่านั้น
    print("string is alpha and numeric = ", s.isalnum()) # สำหรับตรวจตสอบสตริงว่ามีค่าเป็นตัวเลข และตัวอักษร
    print("String is numeric = ", s.isnumeric()) # สำหรับตรวจสอบสตริงว่ามีค่าเป็นตัวเลข
    print("String is decimal = ", s.isdecimal()) # สำหรับตรวจสอบสตริงว่ามีค่าเป็นตำวเลข
    print("String is digit = ", s.isdigit()) # สำหรับตรวจสอบสตริงว่ามีค่าเป็นตัวเลข
    print("String is lower = ", s.islower()) # สำหรับตรวจสอบสตริงว่าเป็นตัวอักษรเล็ก
    print("String is upper = ", s.isupper()) # สำหรับตรวจสอบสตริงว่าเป็นตัวอักษรใหญ่
    print("String is space = ", s.isspace()) # สำหรับตรวจสอบสตริงว่าเป็นช่องว่าง
    print("string is title = ", s.istitle()) # สำหรับตรวจสอบสตริงว่ามีลักษณะเป็น title

    print("\n===34===")
    s = "somchai"
    print(f"Enter string : {s}")
    print()
    print("Lower String = ", s.lower()) # สำหรับแปลงตัวอักษรเป็นตัวอักษรเล็ก
    print("Upper String = ", s.upper()) # สำหรับแปลงตัวอักษรเป็นตัวอักษรใหญ่
    print("Capitalize String = ", s.capitalize()) # สำหรับแปลงตัวอักษรแรกข้องข้อความเป็นตัวอักษรใหญ่
    print("SwapCase String = ", s.swapcase()) # (สลับ) สำหรับแปลงตัวอักษรจากตัวอักษรเล็กเป็นใหญ่ และจากใหญ่เป็นเล็ก

    print("\n===36===")
    s = "Python"
    print(s.count('Py')) # สำหรับนับจนวนจอักขระหรือคำในสตริง
    print(s.find('on')) # สำหรับค้นหาตำแหน่งข้อความในสตริง หากพบจะคืนค่าตำแหน่ง แต่หากไม่พบคืนค่าเป็น -1
    print(s.index("th")) # สำหรับค้นหาตำแหน่งข้อความในสตริง เหมือน find แต่จะแจ้งความผิดพลาดหากไม่พบ
    print(s.replace("thon", "Game")) # สำหรับค้นหาตำแหน่งข้อความในสตริง และแทนค่าตามที่กำหนด

    print("\n===37===")
    s = "somchai cheingpongpan"
    print(f"Enter your name : {s}")
    print("Name capitalize :", s.capitalize()) # สำหรับแปลงตัวอักษรแรกข้องข้อความเป็นตัวอักษรใหญ่
    print("Your name have ")
    print("Find a in name = ", s.count("a")) # สำหรับนับจนวนจอักขระหรือคำในสตริง
    print("Find e in name = ", s.count("e"))
    print("Find i in name = ", s.count("i"))
    print("Find o in name = ", s.count("o"))
    print("Find u in name = ", s.count("u"))
    print("Find \"chai\" in name = ", s.find("chai"))  # สำหรับค้นหาตำแหน่งข้อความในสตริง หากพบจะคืนค่าตำแหน่ง แต่หากไม่พบคืนค่าเป็น -1
    print("Index \"som\" in name = ", s.index("som")) # สำหรับค้นหาตำแหน่งข้อความในสตริง เหมือน find แต่จะแจ้งความผิดพลาดหากไม่พบ
    print("Replace chai with sak : ", s.replace("chai", "sak"))  # สำหรับค้นหาตำแหน่งข้อความในสตริง และแทนค่าตามที่กำหนด

    print("\n===40===")
    s = "Python"
    print(f"Enter your string : {s}")
    print("|" + s.center(10) + "|") # สำหรับจัดข้อความให้อยู่กึ่งกลาง
    print("|" + s.ljust(10, "-") + "|") # สำหรับจัดข้อความให้อยู่ชิดซ้าย
    print("|" + s.rjust(10, "#") + "|") # สำหรับจัดข้อความให้อู๋ชิดขวา

    print("\n===42===")
    s = " somchai Cheingpopngpan python "
    print(f"Enter your string : {s}")
    print("|" + s.strip() + "|") # สรำหรับตัดช่องว่างออกจากสตริงทั้งดา้นซ้ายและขวา
    print("|" + s.lstrip() + "|") # สำหรับตัดช่องว่างออกจากสตริงด้านซ้าย
    print("|" + s.rstrip() + "|") # สำหรับตัดช่องว่างออกจากสตริงด้านขวา
    print(s.join("123")) # สำหรับรวมหรือต่อสตริงหลายๆสตริง
    print(s.split()) # สำหรับตัดแบ่งสตริงเป็นค่าๆ

def ex1():
    # while True:
    #     print()
    #     print("=" * 14)
    #     print("| Main  Menu |")
    #     print("=" * 14)
    #     print(" 1. Triangle 1\n 2. Triangle 2\n 3. Triangle 3\n 4. Triangle 4\n 5. Exit")
    #     choice = int(input("Enter Choice : "))
    #     if choice < 5:
    #         num = int(input("\nEnter number of character : "))
    #         if choice == 1:
    #             for i in range(1,num+1):
    #                 print("*" * i)
    #         elif choice == 2:
    #             for i in range(num,0,-1):
    #                 print("*" * i)
    #         elif choice == 3:
    #             for i in range(1,num+1,+1):
    #                 print(" " * (num - i) +"*" * i)
    #         elif choice == 4:
    #             for i in range(num,0,-1):
    #                 print(" " * (num - i) +"*" * i)
    #     elif choice == 5:
    #         print("\nExit Program ...")
    #         exit()
    #     else:
    #         print("\nInput error choice.")

    #ทำไว้ show ใน terminal
    choice = 1
    num = 5
    while True:
        print()
        print("=" * 14)
        print("| Main  Menu |")
        print("=" * 14)
        print(" 1. Triangle 1\n 2. Triangle 2\n 3. Triangle 3\n 4. Triangle 4\n 5. Exit")
        print(f"Enter Choice : {choice}")
        if choice < 5:
            print(f"\nEnter number of character : {num}\n")
            if choice == 1:
                for i in range(1,num+1):
                    print("*" * i)
            elif choice == 2:
                for i in range(num,0,-1):
                    print("*" * i)
            elif choice == 3:
                for i in range(1,num+1,+1):
                    print(" " * (num - i) +"*" * i)
            elif choice == 4:
                for i in range(num,0,-1):
                    print(" " * (num - i) +"*" * i)
        elif choice == 5:
            print("\nExit Program ...")
            exit()
        else:
            print("\nInput error choice.")
        choice += 1
def ex2():
    # while True:
    #     text = input("Enter text(enter-exit : ")
    #     if text == "":
    #         exit()
    #     elif text.isalpha():
    #         print(f"Text is alphabetic ")
    #     elif text.isdigit():
    #         print(f"Text is digit")
    #     elif text.isalnum():
    #         print(f"Text is alpha and numeric ")
    #     else:
    #         print("Text is String")

    # ทำไว้ show ใน terminal
    text = ["Somchai", "2567", "Python312", "python 3.12",""]
    count = 0
    while True:
        print(f"Enter text(enter-exit : {text[count]}")
        if text[count] == "":
            exit()
        elif text[count].isalpha():
            print(f"Text is alphabetic ")
        elif text[count].isdigit():
            print(f"Text is digit")
        elif text[count].isalnum():
            print(f"Text is alpha and numeric ")
        else:
            print("Text is String")
        count += 1

def ex3():
    # while True:
    #     text = input("Enter text(enter-exit) : ")
    #     if text == "":
    #         exit()
    #     print(f"Text has 'a' : {text.count("a")}")
    #     print(f"Text has 'e' : {text.count("e")}")
    #     print(f"Text has 'i' : {text.count("i")}")
    #     print(f"Text has 'o' : {text.count("o")}")
    #     print(f"Text has 'u' : {text.count("u")}\n")

    # ทำไว้ show ใน terminal
    text = ["This is a girl and boy. You win.","I'm a young programmer, in 2024.",""]
    count = 0
    while True:
        print(f"Enter text(enter-exit) : {text[count]}")
        if text[count] == "":
            exit()
        print(f"Text has 'a' : {text[count].count("a")}")
        print(f"Text has 'e' : {text[count].count("e")}")
        print(f"Text has 'i' : {text[count].count("i")}")
        print(f"Text has 'o' : {text[count].count("o")}")
        print(f"Text has 'u' : {text[count].count("u")}\n")
        count += 1

def ex4():
    # import random                        เกือบถูก
    # ts = 0  # นับผลรวมชั่วคราว
    # t = 0   # นับผลรวมทั้งหมด
    # while True:
    #     # แสดงเมนูหลัก
    #     print("Main  Menu")
    #     print("=" * 9)
    #     print(" 1. Input Number of Score\n 2. Random Score and Check Grade\n 3. Exit")
    #     choice = int(input("Enter Choice : "))
    #     if choice == 1:
    #         # รับจำนวนนักเรียนทั้งหมด
    #         score = int(input("Enter number of score : "))
    #     elif choice == 2:
    #         # เริ่มการสุ่มและตรวจสอบเกรด
    #         print("\nStart Random Score ...")
    #         print("Check Grade ...\n")
    #         print("-" * 14)
    #         print("|Grade| Total|")
    #
    #         remaining = score  # จำนวนนักเรียนที่เหลือที่ต้องจัดสรร
    #         for i in "ABCDF":  # วนลูปผ่านแต่ละเกรด A B C D F
    #             if i == "F":  # ถ้าเป็นเกรด F ให้เอาจำนวนที่เหลือทั้งหมด
    #                 rd = remaining
    #             else:
    #                 # สุ่มจำนวนนักเรียนสำหรับเกรดอื่นๆ (A, B, C, D)
    #                 # จำกัดการสุ่มไม่เกินครึ่งหนึ่งของจำนวนที่เหลือ เพื่อให้มีการกระจายคะแนนที่สมดุล
    #
    #                 # คำนวณจำนวนสูงสุดที่สามารถสุ่มได้ (max_allowed):
    #                 # - remaining คือจำนวนนักเรียนที่ยังไม่ได้ถูกจัดเกรด
    #                 # - // คือการหารแบบปัดเศษทิ้ง เช่น 7 // 2 = 3
    #                 # - if remaining > 1 คือถ้ายังมีนักเรียนเหลือมากกว่า 1 คน
    #                 #   จะใช้ครึ่งหนึ่งของจำนวนที่เหลือ (remaining // 2)
    #                 # - else remaining คือถ้าเหลือ 1 คนหรือน้อยกว่า
    #                 #   จะใช้จำนวนที่เหลือทั้งหมด
    #                 max_allowed = remaining // 2 if remaining > 1 else remaining
    #
    #                 # สุ่มจำนวนนักเรียนในเกรดนี้ (rd):
    #                 # - random.randint(0, max_allowed) คือสุ่มตัวเลขตั้งแต่ 0 ถึง max_allowed
    #                 # - if remaining > 0 คือถ้ายังมีนักเรียนเหลือให้สุ่ม
    #                 # - else 0 คือถ้าไม่มีนักเรียนเหลือแล้วให้กำหนดเป็น 0
    #                 #
    #                 # ตัวอย่าง: ถ้ามีนักเรียน 55 คน
    #                 # - เกรด A: remaining=55, max_allowed=27, rd=สุ่ม(0-27)
    #                 # - เกรด B: remaining=55-rd_A, max_allowed=(55-rd_A)//2, rd=สุ่ม(0-max_allowed)
    #                 # และทำต่อไปจนถึงเกรด D
    #                 rd = random.randint(0, max_allowed) if remaining > 0 else 0
    #
    #             remaining -= rd  # ลดจำนวนที่เหลือ
    #             t += rd         # เพิ่มยอดรวม
    #             print(f"|  {i}  |   {rd:4} |")  # แสดงผลลัพธ์แต่ละเกรด
    #
    #         # แสดงผลรวมทั้งหมด
    #         print("-" * 14)
    #         print(f"|Total|   {t} |")
    #         print("-" * 14)
    #         t = 0  # รีเซ็ตผลรวมสำหรับการรันครั้งต่อไป
    #     elif choice == 3:
    #         break  # ออกจากโปรแกรม

    # import random                 ไม่ใช้
    # ts = 0
    # t = 0
    # start = 1
    # while True:
    #     print("Main  Menu")
    #     print("=" * 9)
    #     print(" 1. Input Number of Score\n 2. Random Score and Check Grade\n 3. Exit")
    #     choice = int(input("Enter Choice : "))
    #     if choice == 1:
    #         score = int(input("Enter number of score : "))
    #     elif choice == 2:
    #         print("\nStart Random Score ...")
    #         print("Check Grade ...\n")
    #         print("-" * 14)
    #         print("|Grade| Total|")
    #         print(f" |{start} {score + 1} {ts} {score + 1 - ts}")
    #         for i in "ABCDF":
    #             if ts == score:
    #                 start = 0
    #
    #
    #             rd = random.randrange(start, score + 1 - ts)
    #             ts += rd
    #             if ts != score and i == "D":
    #                 start = ts -1
    #             # if ts != score and i == "D":
    #             #     ts = 54
    #             t += rd
    #
    #             print(f"|  {i}  |   {rd:4} |{start} {score + 1} {ts} {score + 1 - ts} |{t}")
    #             start = 1
    #         print("-" * 14)
    #         print(f"|Total|   {t} |")
    #         print("-" * 14)
    #         ts = 0
    #         t = 0


    # import random                           comment ไว้เฉยๆ
    # while True:
    #     # แสดงเมนูหลัก
    #     print("Main Menu")
    #     print("=" * 9)
    #     print(" 1. Input Number of Score\n 2. Random Score and Check Grade\n 3. Exit")
    #     choice = int(input("Enter Choice : "))
    #
    #     if choice == 1:
    #         # รับจำนวนคะแนนที่ต้องการสุ่ม
    #         num = int(input("Enter number of score: "))
    #     elif choice == 2:
    #         # เริ่มกระบวนการสุ่มคะแนนและตรวจสอบเกรด
    #         print("\nStart Random Score ...")
    #         print("Check Grade ...\n")
    #         print("-" * 14)
    #         print("|Grade| Total|")
    #
    #         # สร้างตัวแปรสำหรับนับจำนวนเกรดแต่ละระดับ
    #         grades = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    #
    #         # สุ่มคะแนนและตัดเกรด
    #         for i in range(num):
    #             score = random.randint(40, 90)  # สุ่มคะแนนระหว่าง 40-90
    #             if score >= 80:        # ถ้าคะแนน >= 80 ได้ A
    #                 grades['A'] += 1
    #             elif score >= 70:      # ถ้าคะแนน >= 70 ได้ B
    #                 grades['B'] += 1
    #             elif score >= 60:      # ถ้าคะแนน >= 60 ได้ C
    #                 grades['C'] += 1
    #             elif score >= 50:      # ถ้าคะแนน >= 50 ได้ D
    #                 grades['D'] += 1
    #             else:                  # ถ้าคะแนน < 50 ได้ F
    #                 grades['F'] += 1
    #
    #         # แสดงผลการแจกแจงเกรด
    #         total = 0
    #         for g in 'ABCDF':
    #             count = grades[g]
    #             total += count
    #             print(f"|  {g}  |   {count:4} |")
    #
    #         # แสดงผลรวมทั้งหมด
    #         print("-" * 14)
    #         print(f"|Total|   {total} |")
    #         print("-" * 14)
    #
    #     elif choice == 3:
    #         # ออกจากโปรแกรม
    #         print("\nExit Program...")
    #         break



    # import random
    # while True:
    #     # Show main menu
    #     print("Main Menu")
    #     print("=" * 9)
    #     print(" 1. Input Number of Score\n 2. Random Score and Check Grade\n 3. Exit")
    #     choice = int(input("Enter Choice : "))
    #
    #     if choice == 1:
    #         num = int(input("Enter number of score: "))
    #     elif choice == 2:
    #         print("\nStart Random Score ...")
    #         print("Check Grade ...\n")
    #         print("-" * 14)
    #         print("|Grade| Total|")
    #
    #         grades = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    #
    #         for _ in range(num):
    #             score = random.randint(40, 90)
    #             if score >= 80:
    #                 grades['A'] += 1
    #             elif score >= 70:
    #                 grades['B'] += 1
    #             elif score >= 60:
    #                 grades['C'] += 1
    #             elif score >= 50:
    #                 grades['D'] += 1
    #             else:
    #                 grades['F'] += 1
    #
    #         total = 0
    #         for grade in 'ABCDF':
    #             count = grades[grade]
    #             total += count
    #             print(f"|  {grade}  |   {count:4} |")
    #
    #         print("-" * 14)
    #         print(f"|Total|   {total} |")
    #         print("-" * 14)
    #
    #     elif choice == 3:
    #         print("\nExit Program...")
    #         break

    # import random
    # while True:
    #     print("Main  Menu")
    #     print("=" * 10)
    #     print(" 1. Input Number of Score\n 2. Random Score and Check Grade\n 3. Exit")
    #     choice = int(input("Enter Choice : "))
    #     if choice == 1:
    #         num = int(input("Enter number of score : "))
    #     elif choice == 2:
    #         print("'nStart Random Score ...\nCheck Grade ...\n")
    #         print("-" * 14)
    #         print("|Grade| Total|")
    #         print("-" * 14)
    #         grade = ["A","B","C","D","F"]
    #         n_grade = [0,0,0,0,0]
    #         total = 0
    #         for n in range(num):
    #             score = random.randint(40,90)
    #             if score >= 80:
    #                 n_grade[0] += 1
    #             elif score >= 70:
    #                 n_grade[1] += 1
    #             elif score >= 60:
    #                 n_grade[2] += 1
    #             elif score >= 50:
    #                 n_grade[3] += 1
    #             else:
    #                 n_grade[4] += 1
    #         for i in range(len(grade)):
    #             print(f"|  {grade[i]}  |  {n_grade[i]:3} |")
    #             total += n_grade[i]
    #         print("-" * 14)
    #         print(f"|Total|  {total:3} |")
    #         print("-" * 14)
    #     elif choice == 3:
    #         print("Exit Program")
    #         exit()
    #     else:
    #         print("choice not correct.")

    # import random
    # while True:
    #     print("Main  Menu")
    #     print("=" * 10)
    #     print(" 1. Input Number of Score\n 2. Random Score and Check Grade\n 3. Exit")
    #     choice = int(input("Enter choice : "))
    #
    #     if choice == 1:
    #         num = int(input("Enter number of score : "))
    #
    #     elif choice == 2:
    #         print("\nStart Random Score ...")
    #         print("Check Grade ...\n")
    #         grade = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0} #ตัวแปรแบบ dictionary คล้ายๆ list เก็บได้ตั้งค่าต้น และค่าของค่าต้น ใช้ grade["A"] ในการเรียกค่า
    #
    #         for i in range(num):
    #             score = random.randint(40,90)
    #             if score >= 80:
    #                 grade["A"] += 1
    #             elif score >= 70:
    #                 grade["B"] += 1
    #             elif score >= 60:
    #                 grade["C"] += 1
    #             elif score >= 50:
    #                 grade["D"] += 1
    #             elif score >= 40:
    #                 grade["F"] += 1
    #
    #         print("-" * 14)
    #         print("|Grade| Total|")
    #         print("-" * 14)
    #         total = 0
    #
    #         for g in "ABCDF":
    #             print(f"|  {g}  |   {grade[g]:2} |")
    #             total += grade[g]
    #         print("-" * 14)
    #         print(f"|Total|   {total} |")
    #         print("-" * 14)
    #
    #     elif choice == 3:
    #         print("Exit Program")
    #         exit()
    #
    #     else:
    #         pass


    #ทำไว้ show ใน terminal
    import random
    choice = [1,2,1,2,3]
    num = [55,100]
    c = 0
    n= 0
    while True:
        print("Main  Menu")
        print("=" * 10)
        print(" 1. Input Number of Score\n 2. Random Score and Check Grade\n 3. Exit")
        print(f"Enter choice : {choice[c]}")

        if choice[c] == 1:
            print(f"Enter number of score : {num[n]}")

        elif choice[c] == 2:
            print("\nStart Random Score ...")
            print("Check Grade ...\n")
            grade = {"A": 0, "B": 0, "C": 0, "D": 0,
                     "F": 0}  # ตัวแปรแบบ dictionary คล้ายๆ list เก็บได้ตั้งค่าต้น และค่าของค่าต้น ใช้ grade["A"] ในการเรียกค่า

            for i in range(num[n]):
                score = random.randint(40, 90)
                if score >= 80:
                    grade["A"] += 1
                elif score >= 70:
                    grade["B"] += 1
                elif score >= 60:
                    grade["C"] += 1
                elif score >= 50:
                    grade["D"] += 1
                elif score >= 40:
                    grade["F"] += 1

            print("-" * 14)
            print("|Grade| Total|")
            print("-" * 14)
            total = 0

            for g in "ABCDF":
                print(f"|  {g}  |   {grade[g]:2} |")
                total += grade[g]
            print("-" * 14)
            print(f"|Total|   {total} |")
            print("-" * 14)

        elif choice[c] == 3:
            print("Exit Program")
            exit()

        else:
            print("Choice not correct.")
        if c == 1:
            n +=1
        c += 1


s1()