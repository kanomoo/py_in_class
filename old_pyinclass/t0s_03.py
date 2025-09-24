def s():
    print("===9===")
    A = 10
    B = 20
    print("before Swap X = ", A, ", Y= ",B)
    Z = A
    A = B
    B = Z
    print("after  Swap X = ", A, ", Y= ", B)

    a = 10
    b = 20
    print(a,b)
    z = a
    a = b
    b = z
    print(a,b)

    print("\n===10===")
    print(f"10  +  20  = {10 + 20}")  #บวก
    print(f"130 -  10  = {130 - 10}") #ลบ
    print(f"40  *   2  = {40 * 2}")   #คูณ
    print(f"12  /   5  = {12 / 5}")   #หาร
    print(f"12  //  5  = {12 // 5}")  #หารเอาผลจำนวนเต็ม (ตัดเศษ)
    print(f"12  %   5  = {12 % 5}")   #หารเอาเศษ
    print(f"10  **  2  = {10 ** 2}")  #ยกกำลัง

    print("\n===12===")
    # c = 16, d = 4, x = 2.5, y = 0.25
    # วิธีคิด
    # x * y – c / d
    # แทนค่ํา
    # 2.5 * 0.25 – 16 / 4
    # 0.625 – 16 / 4
    # 0.625 – 4.0
    # -3.375
    c, d, x, y = 16, 4, 2.5, 0.25
    print(f"x * y-c /d = {x * y-c /d}")

    print("\n===13===")
    # x = 16, y = 4
    # วิธีคิด - 10 * (x % y – x // (y + 1) )
    # แทนค่ํา - 10 * (16 % 4 - 16 // (4 + 1))
    # -10 * (16 % 4 - 16 // 5)
    # -10 * (0 - 16 // 5)
    # -10 * (0 - 3)
    # -10 * -3
    # 30
    x, y = 16, 4
    print(f"-10 * (x%y-x//(y+1)) = {-10 * (x%y-x//(y+1))}")

    print("\n===14===")
    print(f"10  == 20 = {10 == 20}") # เท่ากับ
    print(f"130 != 10 = {130 != 10}")  #ไม่เท่ากับ
    print(f"40   >  2 = {40 > 2}")  # มากกว่า
    print(f"12   <  5 = {12 < 5}")  # น้อยกว่า
    print(f"12  >=  5 = {12 >= 5}")  # มากกว่าหรือเท่ากับ
    print(f"12  <=  5 = {12 <= 5}")  # น้อยกว่าหรือเท่ากับ

    print("\n===15===")
    a, b, c, = 10, 10.0, 20
    print(f"a == b = {a == b}")
    print(f"b == a = {b == a}")
    print(f"a != b = {a != b}")
    print(f"a != c = {a != c}")
    print(f"a  < c = {a < c}")
    print(f"a  > b = {a > b}")
    print(f"a <= c = {a <= c}")
    print(f"b  < c = {b < c}")
    print(f"b <= c = {b <= c}")
    print(f"5 == '5' = {5 =='5'}")

    print("\n===19===")
    a, b, c, d = 20, 10 ,15, 40
    print(f"a > c and b < d = {a > c and b < d }")
    print(f"a < b and c > d = {a < b and c > d}")
    print(f"a > c or b < d = {a > c or b < d}")
    print(f"a < b or c > d = {a < b or c > d}")
    print(f"a > d and True or b < b = {a > d and True or b < b}")

    print("\n===20===")
    print(f"+= ")  #บวก
    print(f"-= ")  #ลบ
    print(f"*= ")  #คูณ
    print(f"/= ")  #หาร
    print(f"//= ") #หารตัดเศษ
    print(f"%= ")  #หารเอาเศษ
    print(f"**= ") #ยกกำลัง

    print("\n===21===")
    a1,a2,a3,a4,a5,a6,a7 = 5,5,5,5,5,5,5
    a1 += 10
    print(f"(a = 5) --> (a += 10) = {a1}")
    a2 -= 3
    print(f"(a = 5) --> (a -= 3) = {a2}")
    a3 *= 3
    print(f"(a = 5) --> (a *= 3) = {a3}")
    a4 /= 10
    print(f"(a = 5) --> (a /= 10) = {a4}")
    a5 //= 3
    print(f"(a = 5) --> (a //= 3) = {a5}")
    a6 %= 5
    print(f"(a = 5) --> (a %= 5) = {a6}")
    a7 **= 4
    print(f"(a = 5) --> (a **= 4) = {a7}")

    print("\n===23===")
    print(f"7 & 12 = {7 & 12}") # 0111 & 1100 = 0100 = 4  เป็นกํารนำค่าบิตมําทำการ and กัน
    print(f"7 | 12 = {7 | 12}") # 0111 | 1100 = 1111 = 15 เป็นการนำค่าบิตมาทำการ or กัน
    print(f"4 >> 1 = {4 >> 1}") # 0100 >> 1 = 0010 = 2    เป็นการนำค่าบิตมาทำการเลื่อนบิตไปทางขวา
    print(f"4 << 2 = {4 << 2}") # 0100 << 2 = 10000 = 16  เป็ฯการนำค่าบิตมาทำการเลื่อนบิตไปทางซ้าย

    print("\n===24===")
    print(f"'y' in 'Python' = {'y' in 'Python'}") # ตรวจสอบว่าเป็นสมาชิกในข้อมูลใช่หรือไม่
    print(f"'P' not in 'Python' = {'P' not in 'Python'}") # ตรวจสอบว่าไม่เป็นสมาชิกในข้อมูลใช่หรือไม่

    print("\n===25===")
    A = int(10)
    # print("A = 10")
    # print(f"10 is A = {10 is A}") #เป็นการตรวจสอบว่าเป็นวัตถุเดี่ยวกันใช่หรือไม่
    # print(f"10.0 is A = {10.0 is A}")
    # print(f"10.0 is not A = {10.0 is not A}") #เป็นการตรวจสอบว่าไม่เป็นวัตถุเดี่ยวกันใช่หรือไม่
    # print(f"10 is not A = {10 is not A}")
    print("A = 10")
    print(f"10 is A = {10 == A}") #เป็นการตรวจสอบว่าเป็นวัตถุเดี่ยวกันใช่หรือไม่
    print(f"10.0 is A = {10.0 == A}")
    print(f"10.0 is not A = {10.0 != A}") #เป็นการตรวจสอบว่าไม่เป็นวัตถุเดี่ยวกันใช่หรือไม่
    print(f"10 is not A = {10 != A}")

def w1():
    # qty = int(input("Enter number product : "))
    # price = float(input("Price per unit : "))

    # total = price * qty
    # print("Total money : ", total) #ราคารวม

    # pay = float(input("enter pay money : ")) #จ่าย
    # change = pay - total
    # print("Money change : " , change) #เงินทอน

    product = int(input("Enter number product : "))
    price = int(input("Price per unit : "))
    print(f"Total money : {float(product * price)}")
    pay = int(input("Enter pay money : "))
    print(f"Money change : {float(pay - product * price)}")

def w2():
    # num1 = int(input("Enter number 1 : "))
    # num2 = int(input("Enter number 2 : "))
    # print("Before swap num1 = ", num1, "num2 = ", num2)
    # num2 = num1 + num2
    # num1 = num2 - num1
    # num2 = num2 - num1
    # print("After swap num1 = ", num1, "num2 = ", num2)

    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    print(f"Before swap num1 = {num1} , num2 = {num2}")
    # 20 = 10 + 20 (30)
    # 10 = 30 - 10
    # 30 = 30 - 20
    num2 = num1 + num2
    num1 = num2 - num1
    num2 = num2 - num1
    print(f"After  swap num2 = {num1} , num2 = {num2}")
def w3():
    # Score1 = int(input("Enter score 1 : "))
    # Score2 = int(input("Enter score 1 : "))
    # Score3 = int(input("Enter score 1 : "))
    # Score4 = int(input("Enter score 1 : "))
    #
    # Total = Score1 + Score2 + Score3 + Score4
    # Average = Total /4
    # print()
    # print("Total Score : ", Total)
    # print("Average Score : ", Average)
    t_point = 0
    for i in range(1,5):
        point = int(input(f"Enter point {i} : "))
        t_point += point
    print(f"\nTotal Score = {t_point}")
    print(f"Average Score= {t_point / 4}")

def w4():
    # print("Program Calculate Area Circle.")
    # radius = float(input("Enter circle radius (float number) : "))
    # area = 3.14 * radius * radius
    # circum = 2 * 3.14 * radius
    # print("Area of circle with radius", radius, "is", area)
    # print("Circumference is", circum)
    print("Program Calculate Area Circle.")
    radius = float(input("Enter circle radius (float number) : "))
    area = 3.14 * radius * radius
    circum = 2 * 3.14 * radius
    print(f"Area of circle with radius {radius} is {area}")
    print(f"Circumference is {circum}")

def e1():
    # money = int(input("Enter number money withdraw : "))
    # m1 = money // 1000
    # money -= m1 * 1000
    # m2 = money // 500
    # money -= m2 * 500
    # m3 = money // 100
    # money -= m3 * 100
    # print(f"Cash B1000 : {m1}")
    # print(f"Cash B500  : {m2}")
    # print(f"Cash B100  : {m3}")

    # n = int(input("Input :"))
    # print(f"{n % 500}")
    # print(f"1000 : {n // 1000} 500 : {(n % 1000) //  500} 100 : {(n % 500) // 100}")
    # print(f"{n % 500}")

    # num = int(input("Enter number money withdraw : "))
    # print(f"\nCash B1000 : {float(num // 1000)}\nCash B500  : {float(num % 1000 // 500)}\nCash B100  : {float(num % 500 // 100)}"
    #       f"\nCash B50 : {num % 100 //50}\nCash B20 : {num % 50 // 20}\nCash B10 : {num % 20 // 10}\nCash B5 : {num % 10 // 5}"
    #       f"\nCash B2 : {num % 5 // 2}\nCash B1 : {num % 2 // 1}")

    num = int(input("Enter number money withdraw : "))
    print(f"\nCash B1000 : {float(num // 1000)}"
          f"\nCash B500  : {float(num % 1000 // 500)}"
          f"\nCash B100  : {float(num % 500 // 100)}")

def e2():
    # num = int(input("Enter integer number : "))
    # print(num // 1000)
    # print(num % 1000 // 100)
    # print(num % 100// 10)
    # print(num % 10 // 1)

    number = (input("Enter integer number : "))
    print(number[0])
    print(number[1])
    print(number[2])
    print(number[3])

def e3():
    amount = int(input("Enter amount : "))
    rate = float(input("Enter rate : "))
    year = int(input("enter year : "))
    fv = amount * (1 + rate/100) ** year
    print(f"Future value = {fv}")


def e4():
    price = int(input("Enter net price product : "))
    print(f"\nPrice product = {price - price * 7 / 100}")
    print(f"Vat product = {price * 7 / 100}")
    # print(f"Price product : {price - price * 7 / 100}")

s()
