from turtledemo.penrose import start

x_global = 0  # Global variable declaration
def s():
    print("===4===")
    def say_hello():
        print("Hello")
    say_hello()

    print("\n===5===")
    def say_message(text):
        print(text)
    say_message("Hello World")

    print("\n===6===")
    # def sum_number():
    #     sum = 0
    #     for n in range(1, 11):
    #          sum += n
    #     print(f"sum of 1 .. 10 {sum}")
    # print("Program sum 1 to 10 used function.")
    # sum_number()

    def num(num):
        for i in range(num):
            num += i
        print(f"sum of 1 .. 10 = {num}")
    print("Program sum 1 to 10 used function.")
    num(10)

    print("\n===7===")
    # def sum_number(End):
    #     sum = 0
    #     for n in range(1, End + 1):
    #         sum += n
    #     print(f"sum of 1 .. {End} = {sum}")
    # print("Program sum 1 to n used function.")
    # num = int(input("Enter number : "))
    # sum_number(num)

    # def num2(num):
    #     for i in range(num):
    #         num += i
    #     print(f"sum of 1 .. 20 = {num}")
    # print("Program sum 1 to n used function.")
    # num = int(input("Enter number : "))
    # num2(num)

    #ทำไว้ show ใน terminal
    def sum_number(End):
        sum = 0
        for n in range(1, End + 1):
            sum += n
        print(f"sum of 1 .. {End} = {sum}")
    print("Program sum 1 to n used function.")
    num = 20
    print("Enter number : ")
    sum_number(num)

    print("\n===8===")
    # def display_triangle(num, ch):
    #     for n in range(1, num + 1):
    #         message = ""
    #         for m in range(n):
    #              message += ch
    #         print(message)
    # print("Program display triangle.")
    # num = int(input("Enter number line : "))
    # ch = input("Enter character : ")
    # display_triangle(num, ch)

    # def display_triangle(num, ch):
    #     for i in range(1,num+1):
    #         print(str(ch) * int(i))
    # print("Program display triangle.")
    # num = int(input("Enter number line : "))
    # ch = input("Enter character : ")
    # display_triangle(num,ch)

    def display_triangle(num, ch):
        for i in range(1,num+1):
            print(str(ch) * int(i))
    num,ch = 8,"#"
    print("Program display triangle.")
    print(f"Enter number line : {num}")
    print(f"Enter character : {ch}")
    display_triangle(num, ch)

    print("\n===10===")
    def add_value():
        return (20 + 30)
    print(add_value())

    def add_value(a, b):
        return (a +b)
    print(add_value(50,50))

    print("\n===11===")
    # import math
    # def select_menu():
    #     menu = "========\n| Menu |\n========\n"
    #     menu += "1. Circle\n2. Rectangle\n3. Exit\nPlease choose : "
    #     choice = input(menu)
    #     return (choice)
    #
    # def cal_circle(radius):
    #     area = math.pi*radius*radius
    #     return(area)
    #
    # def cal_rectangle(width, height):
    #     area = width * height
    #     return(area)
    #
    # print("Program calculate area.")
    # choice = ""
    # while choice != "3":
    #     choice = select_menu()
    #     if choice == "1":
    #         raduis = float(input("Enter radius : "))
    #         print(f"Area of circle = {cal_circle(raduis):.3f}")
    #     elif choice == "2":
    #         width = float(input("enter width :"))
    #         height = float(input("Enter height : "))
    #         print(f"Area of rectangle = {cal_rectangle(width, height):.3f}")
    #     elif choice == "3":
    #         print("exit Program.")

    # import math
    # def menu():
    #     print("Program calculate area.")
    #     menu = "========\n| Menu |\n========\n1. circle\n2. Rectangle\n3. Exit\nPlease Choose : "
    #     choice = input(menu)
    #     return choice
    #
    # def circle(radius):
    #     area = math.pi * radius * radius
    #     return area
    #
    # def rectangle(width, height):
    #     area = width * height
    #     return area
    # choice = ""
    # while choice != "3":
    #     choice = menu()
    #     if choice == "1" :
    #         radius = float(input("Enter radius : "))
    #         print(f"Area of circle = {circle(radius):.3f}")
    #     elif choice == "2":
    #         width = float(input("Enter width : "))
    #         height = float(input("enter height : "))
    #         print(f"Area of rectangle = {rectangle(width, height):.3f}")
    #     elif choice == "3":
    #         print("Exit Program.")

    #ทำไว้ show ใน terminal
    import math
    def menu():
        print("Program calculate area.")
        menu = f"========\n| Menu |\n========\n1. circle\n2. Rectangle\n3. Exit\nPlease Choose : {choice[count]}"
        print(menu)
        return choice[count]
        # return choice

    def circle(radius):
        area = math.pi * radius * radius
        return area

    def rectangle(width, height):
        area = width * height
        return area
    choice = ["1","2","3"]
    radius = 34.4
    width = 34
    height =  23
    count = 0
    while True:
        choice[count] = menu()
        if choice[count] == "1" :
            print("Enter radius : ")
            print(f"Area of circle = {circle(radius):.3f}")
        elif choice[count] == "2":
            print("Enter width : ")
            print("enter height : ")
            print(f"Area of rectangle = {rectangle(width, height):.3f}")
        elif choice[count] == "3":
            print("Exit Program.")
            break
        count += 1

    print("\n===14===")
    # def check_grade(score):
    #     grade = ""
    #     if score >= 80: grade = "A"
    #     elif score >= 75: grade = "B+"
    #     elif score >= 70: grade = "B"
    #     elif score >= 65: grade = "C+"
    #     elif score >= 60: grade = "C"
    #     elif score >= 55: grade = "D+"
    #     elif score >= 50: grade = "D"
    #     else: grade = "F"
    #     return(grade)
    # print("Program calculate grade.")
    # done = True
    # while done:
    #     score = int(input("enter score ( -1 to exit) : "))
    #     if score >= 0 and score <= 100:
    #         grade = check_grade(score)
    #         print(f"Score {score}, get grade : {grade}")
    #     elif score == -1:
    #         done = False
    #     else:
    #         print("Score error, enter again.")
    # print("Exit program...")

    # def grade(score):
    #     grade = ""
    #     if score >= 80: grade = "A"
    #     elif score >= 75: grade = "B+"
    #     elif score >= 70: grade = "B"
    #     elif score >= 65: grade = "C+"
    #     elif score >= 60: grade = "C"
    #     elif score >= 55: grade = "D+"
    #     elif score >= 50: grade = "D"
    #     else: grade = "F"
    #     return grade
    #
    # print("Program calculate grade.")
    # while True:
    #     score = int(input("Enter score ( -1 to exit) : "))
    #     if score >= 0 and score <= 100:
    #         print(f"Score {score} , get grade : {grade(score)}")
    #     elif score == -1:
    #         print("Exit program...")
    #         break
    #     else: print("Score error, enter again.")

    # ทำไว้ show ใน terminal
    def grade(score):
        grade = ""
        if score >= 80: grade = "A"
        elif score >= 75: grade = "B+"
        elif score >= 70: grade = "B"
        elif score >= 65: grade = "C+"
        elif score >= 60: grade = "C"
        elif score >= 55: grade = "D+"
        elif score >= 50: grade = "D"
        else: grade = "F"
        return grade
    score = [50,60,45,80,77,60,67,72,101,-1]
    count = 0
    print("Program calculate grade.")
    while True:
        print(f"Enter score ( -1 to exit) : {score[count]}")
        if score[count] >= 0 and score[count] <= 100:
            print(f"Score {score[count]} , get grade : {grade(score[count])}")
        elif score[count] == -1:
            print("Exit program...")
            break
        else: print("Score error, enter again.")
        count += 1

    print("\n===17===")
    def add_value(a = 10, b = 20):
        return (a + b)
    print(add_value())
    print(add_value(30))
    print(add_value(30,30))


    print("\n===18===")
    # print("\n===18===")
    # def print_triangle(num = 5):
    #     for n in range(1, num + 1):
    #         text = "#" * n
    #         print(text)
    # print()
    # print_triangle()
    # print()
    # print_triangle(3)
    # print()
    # print_triangle(8)

    def triangle(num = 5):
        for i in range(1, num + 1):
            print("#" * i)
        print()
    triangle()
    triangle(3)
    triangle(8)


    print("\n===21===")
    # def factorial1(number):
    #     fac = 1
    #     for n in range(1, number + 1):
    #         fac = fac * n
    #     return(fac)
    #
    # def factorial2(number):
    #     if number > 0:
    #         return(number * factorial2(number - 1))
    #     else:
    #         return(1)
    #
    # num = int(input("Enter number : "))
    # print("Factorial1 with for = ", factorial1(num))
    # print("Factorial2 with recursive = ", factorial2(num))

    # def factorial1(num):
    #     n = 1
    #     for i in range(1, num + 1):
    #         n = i * n
    #     return(n)
    #
    # def factorial2(num):
    #     if num > 0:
    #         return(num * factorial2(num - 1))
    #     else:
    #         return 1
    # num = int(input("Enter number : "))
    # print(f"Factorial1 with for = {factorial1(num)}")
    # print(f"Factorial2 with recursive = {factorial2(num)}")

    # ทำไว้ show ใน terminal
    def factorial1(num):
        n = 1
        for i in range(1, num + 1):
            n = i * n
        return(n)

    def factorial2(num):
        if num > 0:
            return(num * factorial2(num - 1))
        else:
            return 1

    num = 5
    print("Enter number : ")
    print(f"Factorial1 with for = {factorial1(num)}")
    print(f"Factorial2 with recursive = {factorial2(num)}")


    print("\n===24===")
    # ประกาศตัวแปร global x และกำหนดค่าเริ่มต้น
    global x
    def show_local():
        global x  # บอกว่าจะใช้ตัวแปร global x ตัวแปรที่ถูกกำหนดไว้ภายนอกฟังก์ชันะสามารถเข้าถึงได้จากทุกส่วนของโปรแกรม
        y = 10
        x = x + y  # ตอนนี้สามารถใช้และแก้ไขค่า x ได้
        print("x = ", x)
        print("y = ", y)

    x = 5
    show_local()
    print(x)

    print("\n===25===")
    # # ลบ global declaration ที่อยู่นอกฟังก์ชันออก
    #
    # def enter_data():
    #     global total, num1  # ประกาศ global ไว้ในฟังก์ชัน
    #     total = num1 = value = 0
    #     while value != -1:
    #         value = int(input(f"Enter value {num1 + 1} : "))
    #         if value != -1:
    #             total += value
    #             num1 += 1
    #
    # # กำหนดค่าเริ่มต้นให้ตัวแปรก่อนเรียกใช้ฟังก์ชัน
    #
    # enter_data()
    # print(f"number or value : {num1}")
    # print(f"Total number : {total}")
    # print(f"Average value : {total/num1}")

    # def enter_data():
    #     global total, num, value #ตัวแปรที่ถูกกำหนดไว้ภายนอกฟังก์ชันะสามารถเข้าถึงได้จากทุกส่วนของโปรแกรม
    #     total = num = value = 0
    #     while num != -1:
    #         num = int(input(f"Enter value {value + 1} : "))
    #         if num != -1:
    #             value += 1
    #             total += num
    # enter_data()
    # print(f"number of value : {value}")
    # print(f"Total number : {total}")
    # print(f"Average value : {total / value}")


    # ทำไว้ show ใน terminal เฉยๆ
    def enter_data():
        global total, num, value #ตัวแปรที่ถูกกำหนดไว้ภายนอกฟังก์ชันะสามารถเข้าถึงได้จากทุกส่วนของโปรแกรม
        total = value = 0
        num = [67,55,88,45,57,89,78,90,66,-1]
        while True:
            print(f"Enter value {value + 1} : {num[value]}")
            if num[value] != -1:
                total += num[value]
            if num[value] == -1:
                break
            value += 1
    enter_data()
    print(f"number of value : {value}")
    print(f"Total number : {total}")
    print(f"Average value : {total / value}")

def w():
    import w7.Modules
    import w7.Modules as m
    from w7.Modules import draw_triangle
    menu = "Main Menu\n" + ("=" * 10) + "\n1. Sum Number\n"
    menu += "2. Factorial\n3. Draw Triangle\n4. Exit\nEnter Choice : "
    while True:
        choice = input(menu)
        match choice:
            case "1":
                sum = w7.Modules.sum_number(10, 40)
                print("\nSum 10 - 40 = ", sum, "\n")
            case "2":
                fac = m.factorial(7)
                print("\nFactorial(7) = ", fac, "\n")
            case "3":
                print()
                draw_triangle("#", 10)
                print()
            case "4":
                print("Exit Program...")
                break
            case _ : # ทั้งหมด
                print("No choice.")


    # ทำเอง
    # import w7.Modules as m
    # while True:
    #     choice = input(f"Main Menu\n{"=" * 10}\n1. Sum Number\n2. Factorial\n3. Draw Triangle\n4. Exit\nEnter Choice : ")
    #     match choice:
    #         case "1":
    #             m.sum()  # เรียกใช้โดยตรงไม่ต้อง print
    #         case "2":
    #             m.factorial()
    #         case "3":
    #             m.triangle()
    #         case "4":
    #             print("Exit Program...")
    #             break
    #         case _ :
    #             print("No choice.\n")
def find_max(num):
    # return max(str(num))
    max = 0
    for i in str(num):
        if int(i) >= int(max):
            max = i
    return max

def ex1():
    print(find_max(6378942))


def check_palindrome(num):
    # if num[0] == num [-1]:
    #     print("True")
    # if num[1] == num [-2]:
    #     print("True")
    count = 0
    count2 = -1
    p = ""
    for i in num:
        if num[count] == num[count2]:
            p = "True"
            count += 1
            count2 -= 1
        elif num[count] != num[count2]:
            p = "False"
            pass
    return p

def ex2():
    print(check_palindrome("1906091"))


def num_to_text(num):
    num = 638342
    p = ""
    for i in str(num):
        if i == "9": p += "NINE "
        elif i == "8": p += "EIGHT "
        elif i == "7": p += "SEVEN "
        elif i == "6": p += "SIX "
        elif i == "5": p += "FIVE "
        elif i == "4": p += "FOUR "
        elif i == "3": p += "THREE "
        elif i == "2": p += "TWO "
        elif i == "1": p += "ONE "
        elif i == "0": p += "ZERO "
    return p

def ex3():
    print(num_to_text(638342))



# def dec_to_bin(num):
#     if num == 0:
#         return "0"
#
#     binary = ""
#     while num > 0:
#         binary = str(num % 2) + binary
#         num //= 2
#
#     # เพิ่มช่องว่างทุก 4 หลัก
#     result = ""
#     count = 0
#     for i in range(len(binary)-1, -1, -1):
#         result = binary[i] + result
#         count += 1
#         if count == 4 and i != 0:
#             result = " " + result
#             count = 0
#
#     return result

# def dec_to_bin(num):
#     num = bin(num)
#     count = 0
#     p = ""
#     p2 = ""
#     l = len(num)
#     # for i in num[2: ]:
#     #     p += i
#     #     count += 1
#     #     if count % 4 == 0:
#     #         p += " "
#     for i in range(l-1,-1,-1):
#         p += num[i]
#         count += 1
#         if count % 4 == 0:
#             p += " "
#     l2 = len(str(p))
#
#     for i in range(l2-1,-1,-1):
#         p2 += p[i]
#     return p2[3:]

# def dec_to_bin(num):
#     num = bin(num)
#     count = 0
#     p = ""
#     l = len(num)
#     for i in range(l-1,-1,-1):
#         p += num[i]
#         count += 1
#         if count % 4 == 0:
#             p += " "
#     return p[::-1][3:]

def dec_to_bin(num):
    p = ""
    count = 0
    num = bin(num)
    for i in num[2:][::-1]:
        p += i
        count += 1
        if count == 4:
            p += " "

            count = 0
    return p[::-1]

def ex4():
    print(dec_to_bin(1829463))



def assignment5():
    import w7.Myfew as m
    while True:
        choice = input("Program Test Call Module\nMain Menu\n1. Find Max Number\n2. Check Palindrome\n3. Number to Text\n4. Decimal TO Binary\n5. Exit\nEnter Choice : ")
        match choice:
            case "1":
                m.Max()
            case "2":
                m.palindrome()
            case "3":
                m.num_text()
            case "4":
                m.binary()
            case "5":
                print("Exit Program.")
                break
            case _ :
                print("No choice.")
assignment5()