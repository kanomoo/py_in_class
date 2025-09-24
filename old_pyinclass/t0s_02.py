def s():
    import keyword
    print("===9===")
    print(keyword.kwlist,"\n")

    print("===14===")
    name = "somchai"
    print(name)
    name = 78
    print(name)
    name = 3.14
    print(name)

    print("\n===15===")
    Name = "Guido van Rossum"
    Message1 = "Pythong invented by " + Name + " in 1989" #บวกstring
    print(Message1)
    Ver = 3.9
    Str = "Python " + str(Ver) #ทำให้verเป็นstringแล้วบวก string
    print(Str)

    print("\n===17===")
    print("Line 1\nLine 2\nLine 3") # \n = ขึ้นบรรทัดใหม่
    print()
    print("Col 1\tCol 2\tCol3") # \t = tab
    print("c:\\windows\\system") # \\ = \
    print("Name :\"Somchai Cheingpongpan\"") # \" = "  and  \' = '
    print(" This 's Python. ")
    print("\x48\145\154\x6C\157") # \x-- = เลขฐาน16 and \--- = เลขฐาน 8

    print("\n===18===")
    input_name = input("Enter your name : ") #input กรอกข้อมูล
    print("Your input name :", input_name)

    print("\n===20===")
    # str_int = input("Input integer number : ") #basic
    # num_int = int("str_int")
    num_int = int(input("Input integer number : ")) #กำหนดค่าในการinput
    num_float = float(input("Input float number : "))

def e1():
    # print("\n===21===")
    # name = input("Enter name : ")                               #basic -_-
    # surname = input("Enter surname : ")
    # age = int(input("Enter age : "))
    # print("\nMy name is", name)
    # print("My surname is", surname)
    # print(f"Now i'm", age, "years old.")
    # print("I'll finish undergraduate in", age + 4 ,"years old.")

    name = input("Enter name : ")
    surname = input("Enter surname : ")
    age = int(input("Enter age : "))
    print(f"\nMy name is {name}")
    print(f"My surname is {surname}")
    print(f"Now i'm {age} years old.")
    print(f"I'll finish undergraduate in {age + 4} years old.")

def e2():
    # num1 = int(input("Enter integer number1 : "))     #ิbasic
    # num2 = int(input("Enter integer number2 : "))
    # num3 = int(input("Enter integer number2 : "))
    # print("\nValue number1 :", num1)
    # print("Value number2 :", num2)
    # print("Value number3 :", num3)
    # print("Total all :", (num1+num2+num3))

    #แบบ เบียว
    num_l = []  # สร้าง list สำหรับเก็บข้อมูลหมายเลขและค่าที่ผู้ใช้ป้อน
    total_num = 0  # ตัวแปรสำหรับเก็บผลรวมของค่าที่ป้อนทั้งหมด
    for i in range(1, 4):  # ทำซ้ำ 3 รอบ โดย i จะมีค่าเป็น 1 ถึง 3
        num = int(input(f"Enter integer number{i} : "))  # รับค่าจากผู้ใช้เป็นจำนวนเต็ม พร้อมแสดงหมายเลขรอบ โดยใช้ f_string
        num_l.append((i, num))  # เพิ่ม tuple (รอบ, ค่าที่ป้อน) ลงใน list ใดยใช้ append
        total_num += num  # บวกค่าที่ป้อนเข้าไปในผลรวม
        if i == 3:  # เมื่อถึงรอบสุดท้าย (รอบที่ 3) ให้เว้นบรรทัด
            print("")
    for l in num_l:  # แสดงผลลัพธ์ทั้งหมดใน list ที่เก็บไว้ โดยใช้ for l เพื่อทำให้ num_l เป็น f_string ทำให้ () ใน list หายไป
        print(f"Value number{l[0]} : {l[1]}")  # แสดงหมายเลขรอบและค่าที่ผู้ใช้ป้อน
    print(f"Total all : {total_num}")  # แสดงผลรวมของค่าทั้งหมด

def e3():
    # float1 = float(input("Enter float number1 : "))     #ิbasic
    # float2 = float(input("Enter float number2 : "))
    # float3 = float(input("Enter float number2 : "))
    # print("\nValue number1 :", float1)
    # print("Value number2 :", float2)
    # print("Value number3 :", float3)
    # print("Total all :", (float1+float2+float3))

    # แบบ เบียว
    num_f_l = []
    t_float = 0
    for i in range(1,4):
        num_f = float(input(f"Enter float number{i} : "))
        num_f_l.append((i, num_f))
        t_float += num_f
        if i == 3:
            print("")
    for l in num_f_l:
        print(f"Value number{l[0]} : {l[1]}")
    print(f"Total all : {t_float}")

def e4():
    # print("Program Calculate Area Rectangle.")
    # length = int(input("Enter length : "))
    # width = int(input("Enter width : "))
    # area = length * width
    # print("\nArea of Rectangle =", area)

    print("Program Calculate Area Rectangle.")
    length = int(input("Enter length : "))
    width = int(input("Enter width : "))
    print(f"\nArea of Rectangle = {length * width}")

s(), e1(), e2(), e3(), e4()