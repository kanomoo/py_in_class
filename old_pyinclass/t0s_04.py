from numpy.ma.extras import average


def s():
    print("===3===")
    print(-10) #แสดงค่าข้อมูลตามที่กำหนด
    print(type(3)) #ตรวจสอบประเภทข้อมูล
    print(str(22)) #แปลค่าตัวเลขเป็นข้อความ
    print(int("22")) #แปลงข้อความเป็นค่าตัวเลขจำนวนเต็ม
    print(float("35.5")) #แปลงข้อความเป็นค่าตัวเลขทศนิยม
    # input("enter name :") #รับข้อมูลทางคีย์บอร์ดเป็นชนิด String

    print("\n===4===")
    print(abs(-10)) #หาค่าสัมบูรณ์ของตัวเลขที่กำหนด
    print(pow(3,3)) #หาค่ายกกำลังมีผลลัพธ์ตามประเภทที่กำหนด
    print(max(10, 40, 20)) #หาค่าตัวเลขที่มากที่สุด
    print(min(10, 40, 20)) #หาค่าตัวเลขที่น้อยที่สุด
    print(round(4.7)) #การปัดเศษ
    print(round(4.5, 0))
    print(round(4.51, 0))
    print(round(4.35, 1))
    print(round(4.353, 1))
    print(round(4.386, 2))

    print("\n===5===")
    print(chr(65))  #แปลงค่า Ascii เป็นอักขระ
    print(ord("0")) #แปลงค่าอักขระเป็น Ascii เลข

    print(bin(12))  #แปลงค่าเลขฐานสิบเป็นเลขฐานสองแบบข้อความ
    print(bin(24))

    print(oct(65))  #แปลงค่าเลขฐานสิบเป็นเลขฐานแปดแบบข้อความ
    print(oct(128))

    print(hex(65))  #แปลงค่าเลขฐานสิบเป็นเลขฐานสิบหกแบบข้อความ
    print(hex(128))

    print(len("python"))  #การนับจำนวนข้อมูลตามชนิดที่ส่งมา
    print(len(("One", 12, 3.14)))
    print(len(["One", 12, 3.14]))

    print("\n===6===")
    print(sum([10,20,30])) #การหาผลรวมของตัวเลข
    print(eval("10+30"))   #การแปลความหรือทำงานตามคำสั่ง string-expression แปลงstringเป็น สูตร
    print(eval("5+3*4"))
    print(eval("5 > 4 and True"))
    print(eval("2 << 2"))
    print(eval("2 << 4 > 2 ** 4"))


    print("\n===7===")
    import math
    print(math.ceil(7.3))  #หาค่าจำนวนเต็มที่มีค่ามากใกล้กับค่าที่กำหนด
    print(math.floor(7.8)) #หาค่าจำนวนเต็มที่น้อยใกล้กับค่าที่กำหนด
    print(math.fabs(-290.30)) #หาค่าสัมมบูรณ์ชนิดจำนวนทศนิยม
    print(math.factorial(5))  #หาค่า factorial
    print(math.pow(5, 3)) #หาค่ายกกำลัง ผลลัพย์เป็นทศนิยม
    print(math.sqrt(9))         #หาค่ารากที่สอง ผลลัพธ์เป็นทศนิยาม
    print(math.trunc(19.67))    #หาค่าปัดเศษทิ้ง ผลลัพธ์เป็นจำนวนเต็ม

    print("\n===8===")
    print(math.sin(1.5)) #หาค่าตรีโกณมิติของ sin
    print(math.cos(1.5)) #หาค่าตรีโกณมิติของ cos
    print(math.tan(1.5)) #หาค่าตรีโกณมิติของ tan
    print(math.degrees(1.5)) #หาค่ามุมหน่วยเป็นองศาจากค่าเรดียน
    print(math.radians(90)) #หาค่ามุมหน่วยเป็นเรเดียนจากค่าองศา
    print(math.exp(1)) #หาค่ายกกำลังของ e

    print("\n===9===")
    print(math.log(5))   #หาค่า logarithm ของฐาน e
    print(math.log10(5)) #หาค่า logarithm ของฐานสิบ
    print(math.log2(5))  #หาค่า logarithm ของฐานสอง
    print(math.gcd(42, 8)) #หาค่าตัวหารร่วมมาก(ห.ร.ม)
    print(math.lcm(20, 8)) #หาค่าตัวคูณร่วมน้อย(ค.ร.น)
    print(math.e)  #ค่า e
    print(math.pi) #ค่า pi

    print("\n===10===")
    import random
    print(random.random())            #สุ่มค่าเป็นตัวเลขทศนิยม 0.0 - 1.0
    print(random.uniform(1, 4)) #สุ่มค่าเป็นตัวเลขทศนิยมระหว่าง a ถึง b
    print(random.randint(1, 6)) #สุ่มค่าเป็นตัวเลขจำนเต็มระหว่าง a ถึง b
    print(random.choice([1,2,3,4,5,6,7,])) #สุ่มค่าข้อมูลจากในวงเล็บ(sequence) มาหนึ่งค่า
    print(random.randrange(1,10,5))  #ส่มค่าข้อมูลจาก sequence มาหนึีงค่าระหว่าง start ถึง stop โดยเว็นค่าตาม step

    print("\n===11===")
    import datetime
    print(datetime.datetime(2024,7,1)) #สร้างข้อมูลวันเวลา
    print(datetime.date(2020, 2, 4)) #สร้างข้อมมูลวัน
    print(datetime.time(20,10,11)) #สร้างข้อมูลวั

    print("\n===12===")
    print(datetime.datetime.now()) #สร้างข้อมูลวันและเวลาปัจจุบัน โดยเรียนใช้ผ่าน datetime
    print(datetime.datetime.today()) #สร้างข้อมูลวันเและเวลา ปัจจุบัน โดยเรียนกใช้ผ่าน datetime

    date = datetime.datetime.today() #เป็นการกำหนดรูปแบบแสดงผลของวันเวลา
    print(date.strftime("%d %B %Y"))

    print("\n===13===")
    print(date.strftime("%a")) #ย่อวัน
    print(date.strftime("%A")) #วัน
    print(date.strftime("%w")) #วัน 0-6
    print(date.strftime("%d")) #วันที่
    print(date.strftime("%b")) #ชื่อเดือนย่อ
    print(date.strftime("%B")) #ชื่อเดือน
    print(date.strftime("%m")) #เลขเดือน
    print(date.strftime("%y")) #เลขปีย่อ
    print(date.strftime("%Y")) #เลขปี
    print(date.strftime("%H")) #ชั่วโมง 00-23
    print(date.strftime("%I")) #ชั่วโมง 00-12
    print(date.strftime("%p")) #AM/PM
    print(date.strftime("%M")) #นาที
    print(date.strftime("%S")) #วินาที

    print("\n===14===")
    print(date.strftime("%f")) #microsecond
    print(date.strftime("%z"))  #ส่วนเบี่ยงเบนเวลา
    print(date.strftime("%Z"))  #Timezone
    print(date.strftime("%j"))  #วันที่ 1-365
    print(date.strftime("%U"))  #สัปดาที่เท่าไหร่ของปีนับจากวันอาทิตย์
    print(date.strftime("%W"))  #สัปดาที่เท่าไหร่ของปีนับจากวันจันทร์
    print(date.strftime("%c"))  #local version of date and time
    print(date.strftime("%C"))  #ศตวรรษ
    print(date.strftime("%x"))  #local version of date
    print(date.strftime("%X"))  #local version of time
    print(date.strftime("%%"))  #%
    print(date.strftime("%G"))  #ปีมาตรฐาน
    print(date.strftime("%u"))  #วันที่ในสัปดาห์มาตรฐาน
    print(date.strftime("%V"))  #สัปดาห์ที่มาตรฐาน

    print("\n===15===")
    print(format(12345,','))   #ให้มีคอมม่า (,) คั่าหลักพัน
    print(format(12345,'.1f')) #กำหนดตัวเลขทศนิยม ? เป็นจำนวนทศนิยมใช้คู่กับ f
    print(format(0.25,'.0%'))  #แปลฃตัวเลขนิยมเป็นเปอร์เซ็นต์ ? เป็ฯจำนวนทศนิยมและผลลัพธ์จะมี % ต่อท้าย
    print(format(123,'0>5'))   #เป็นการเติมอักขระ ? ไว้ด้านซ้าย หากจำนนวตัวเลขไม่ครบ n โดย ? เป็นอักขระและ n เป็นตัวเลข
    print(format(123,'0<5'))   #เป็นการเติมอักขระ ? ไว้ด้านขวา หากจำนวนตัวเลขไม่ครบ n โดย ? เป็นอักขระและ n เป็นตัวเลข

def w1():
    baseInt = int(input('ใส่ค่าเลขฐานจำนวนเต็ม : '))
    expInt = int(input('ใส่ค่ายกกำลังจำนวนเต็ม : '))
    result = pow(baseInt, expInt)
    print("ค่ายกกำลังของ", baseInt, '^', expInt, '=', result)
    print()

    basefloat = float(input('ใส่ค่าเลขฐานจำนวนทศนิยม : '))
    expfloat = float(input('ใส่ค่ายกกำลังจำนวนทศนิยม : '))
    result = pow(basefloat, expfloat) #หาค่ายกกำลังมีผลลัพธ์ตามประเภทที่กำหนด
    print("ค่ายกกำลัง", basefloat, '^', expfloat,end='')
    print(' = ', result, '->',round(result,2)) #การปัดเศษ

def w2():
    num1 = int(input("Enter value number1 : "))
    num2 = int(input("Enter value number2 : "))
    num3 = int(input("Enter value number3 : "))
    MinValue = min(num1, num2, num3)
    MaxValue = max(num1, num2, num3)

    print()
    print("Your enter number : ", num1, num2, num3)
    print("Maximum value : ", MaxValue)
    print("Minimum value : ", MinValue)
    print("Average value : ", round(sum((num1,num2,num3))/3,2)) #หาค่าเฉลี่ยและปัดเศษ

def w3():
    ch = input("Enter charater : ")

    print("Charater ", ch, " has ascii value ", ord(ch)) #แปลงค่าอักขระเป็น Ascii
    print("Ascii value ", ord(ch), " has charater value ", chr(ord(ch)) ) # chr(ord(ch)) ทำให้เป็นอักขระเหมือนเดิม
    print()
    num = ord(ch)
    print("Decimal value : ", num)
    print("Binary value : ", bin(num)) #แปลงค่าเลขฐานสิบเป็นเลขฐานสอง  แสดงเป็น string
    print("Octal value : ", oct(num))  #แปลงค่าเลขฐานสิบเป็นเลขฐานแปด  แสดงเป็น string
    print("Hexa value : ", hex(num))   #แปลงค่าเลขฐานสิบเป็นเลขฐานสิบหก แสดงเป็น string

def w4():
    import math
    fnum = float(input("Enter float number : "))
    print()
    print("Ceil number : ", math.ceil(fnum)) #หาค่าจำนวนเต็มที่มีค่ามากใกล้กับค่าที่กำหนด
    print("Float number : ", math.floor(fnum)) #หาค่าจำนวนเต็มที่น้อยใกล้กับค่าที่กำหนด
    print("Sqrt number : ", math.sqrt(fnum))  #หาค่ารากที่สอง ผลลัพธ์เป็นทศนิยาม
    print("Trunc number : ", math.trunc(fnum)) #หาค่าปัดเศษทิ้ง ผลลัพธ์เป็นจำนวนเต็ม

    num = math.trunc(fnum)
    print("Degree Angle : ", num)
    print("Radians Angle : ", math.radians(num)) #หาค่ามุมหน่วยเป็นเรเดียนจากค่าองศา
    print("sin  : ", math.sin(math.radians(num))) #หาค่าตรีโกณมิติของ sin
    print("cos  : ", math.cos(math.radians(num)))  # หาค่าตรีโกณมิติของ cos
    print("tan  : ", math.tan(math.radians(num)))  # หาค่าตรีโกณมิติของ tan

def w5():
    import math
    num1 = int(input("Enter integer number 1 : "))
    num2 = int(input("Enter integer number 2 : "))
    gcdNum = math.gcd(num1, num2) #หาค่าตัวหารร่วมมาก(ห.ร.ม)
    lcmNum = math.lcm(num1, num2) #หาค่าตัวคูณร่วมน้อย(ค.ร.น)
    print()
    print("Integer number ", num1, " and ", num2)
    print("Greatest Common Divisor = ", gcdNum)
    print("Least Common Multiple. = ", lcmNum)
    print()
    print("Factorial ", num1, "! is value ", math.factorial(num1)) #หาค่า factorial
    print("Factorial ", num2, "! is value ", math.factorial(num2))

def w6():
    import random
    a = random.randint(1, 10) #สุ่มค่าเป็นตัวเลขจำนเต็มระหว่าง a ถึง b
    print("random value 1, 10 = ", a)
    a = random.randint(40, 100)
    print("random value 40, 100 = ", a)
    print()
    b = random.random() #สุ่มค่าเป็นตัวเลขทศนิยม 0.0 - 1.0
    print("random float value 0.000 - 0.999 = ", b)
    print()
    c = random.uniform(1.5, 8.5) #สุ่มค่าเป็นตัวเลขทศนิยมระหว่าง a ถึง b
    print("c = ", c)
    print()
    d= random.choice("Python") #สุ่มค่าข้อมูลจากในวงเล็บ(sequence) มาหนึ่งค่า
    print("random data from specific = ", d)
    print()
    e = random.randrange(10, 101, 10) #ส่มค่าข้อมูลจาก sequence มาหนึีงค่าระหว่าง start ถึง stop โดยเว็นค่าตาม step
    print("random 10 - 100 step 10 = ", e)

def w7():
    import datetime
    now = datetime.datetime.now() #สร้างข้อมูลวันและเวลาปัจจุบัน โดยเรียนใช้ผ่าน datetime
    print("Default : ", now)
    print("C Time Style : ", now.ctime())
    print("ISO Time : ", now.isoformat())
    print()
    print("ปี : ", now.strftime("%y %Y"))
    print("เดือน : ", now.strftime("%m %b %B"))
    print("วันที่ : ", now.strftime("%d %a %A"))
    print("ชั่วโมง : ", now.strftime("%H %I %p"))
    print("นาที : ", now.strftime("%M"))
    print("วินาที : ", now.strftime("%S"))
    print("ไม่โครวินาที : ", now.strftime("%f"))
    print()
    print("วันที่ : ", now.strftime("%d/%m/%Y"))
    print("วันที่แบบย่อ : ", now.strftime("%d %b %y"))
    print("วันที่แบบเต็ม : ", now.strftime("%d %B %Y"))
    print()
    print("เวลา : ", now.strftime("%H:%M:%S"))
    print("เวลา : ", now.strftime("%I:%M:%S %p"))

def w8():
    price = 12_345.00
    qty =int(input("Enter quantity product : "))
    print()
    total = price * qty
    print("Total price : ", format(total, ',.2f'))
    vat = total * 0.07
    print("Vat (7%) : ", format(vat,',.2f'))
    allTotal = total + vat
    print("All total : ", format(allTotal, ',.2f'))
    print("All total : ", format(allTotal, '#>20,.2f'))

def e1():
    import math
    print("Equation 1 : sin x ^2 + cos x ^ 2")
    x = float(input("Enter value x (degree angle) : "))  #56.4
    print("x = ", x)
    e1 = format((math.sin(x) ** 2 + math.cos(x) ** 2),".8f")
    print("value of sin x ^2 + cos x ^ 2 is ", e1,"\n")

    print("Equation 2 : e^(0.5 sqrt(tan cos x)")
    x = float(input("Enter value x (degree angle <= 90) : ")) #23.7
    x_rad = math.radians(x)
    print("x = ", x)
    e2 = math.exp(0.5 * math.sqrt(math.tan(math.cos(x_rad))))
    print("value of e^(0.5 sqrt(tan cos x)is = ", e2,"\n")

    print("Equation 3 : [ log(x^2/(1-x)) ] / [ x^(5+x) ]")
    x = float(input("Enter value x (0.0 - 1.0) : "))   #0.345
    print("x = ", x)
    e3 = math.log10((x ** 2 / (1 - x))) / (x ** (5 + x))
    print("value of [ log(x^2/(1-x)) ] / [ x^(5+x) ] is ", e3)



def e2():
    import random
    r1 = float(format(random.uniform(30, 50), ".2f"))
    r2 = float(format(random.uniform(30, 50), ".2f"))
    r3 = float(format(random.uniform(30, 50), ".2f"))
    r4 = float(format(random.uniform(30, 50), ".2f"))
    r5 = float(format(random.uniform(30, 50), ".2f"))
    print(f"Value random : {r1} , {r2} , {r3} , {r4} , {r5}")
    total = float(format(r1 + r2 + r3 + r4 + r5,".2f"))
    print("Total value : ", total)
    r_average = float(format(r1 + r2 + r3 + r4 + r5 / 5,".2f"))
    print("Average value : ",r_average)


    # import random
    # tr = []
    # for i in range(6):
    #     r = random.uniform(30,50) #สุ่มค่าเป็นตัวเลขทศนิยมระหว่าง a ถึง b
    #     tr.append(r) #เพิ่มใน list
    # total = (tr[0]+ tr[1]+ tr[2]+ tr[3] +tr[4])
    # print(f"Value random : {tr[0]:.2f} , {tr[1]:.2f} , {tr[2]:.2f} , {tr[3]:.2f} , {tr[4]:.2f}")
    # print(f"Total value {total:.2f}")
    # print(f"Average value : {total / 5:.2f}")

s()