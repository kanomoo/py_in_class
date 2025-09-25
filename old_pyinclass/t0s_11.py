from itertools import count


def s():
    print("===3===") ##################################################################################
    # Exception คือเหตุการณ์ผิดปกติที่เกิดขึ้นในระหว่างการประมวลผลโปรแกรม
    # ทำให้โปรแกรมไม่สามารถทำงานตามที่กำหนดได้

    # ลักษณะของ Exception ที่พบบ่อย เช่น

    #  การหารด้วยตัวเลข 0
    #  การเปิดไฟล์เพื่ออ่านที่ไม่มีอยู่จริง
    #  การแปลงค่าข้อความไปเป็นตัวเลข

    # 5 / 0 error

    print("\n===4===") #####################################################################
    # การจัดการ Exception ด้วย try-except

    # ในภาษา Python เราสามารถดักจับข้อผิดพลาด (Exception)
    # ที่อาจเกิดขึ้นระหว่างการทำงานของโปรแกรมได้
    # โดยใช้คำสั่ง try-except ซึ่งจะช่วยให้โปรแกรมไม่หยุดทำงานทันทีเมื่อเกิดข้อผิดพลาด
    # และสามารถจัดการข้อผิดพลาดนั้นได้อย่างเหมาะสม

    # รูปแบบการใช้งาน:
    # try:
    #     # คำสั่งที่อาจเกิดข้อผิดพลาด
    # except ชนิดของข้อผิดพลาด:
    #     # คำสั่งเมื่อเกิดข้อผิดพลาด

    # ตัวอย่าง:
    # try:
    #     number = int(input("ป้อนตัวเลข: "))
    #     result = 10 / number
    #     print("ผลลัพธ์คือ", result)
    # except ValueError:
    #     print("กรุณาป้อนเป็นตัวเลขเท่านั้น")
    # except ZeroDivisionError:
    #     print("ไม่สามารถหารด้วยศูนย์ได้")

    # อธิบาย:
    # ถ้าผู้ใช้ป้อนค่าที่ไม่ใช่ตัวเลข จะเกิด ValueError
    # ถ้าผู้ใช้ป้อนเลข 0 จะเกิด ZeroDivisionError
    # โปรแกรมจะไม่หยุดการทำงานทันที แต่จะเข้าสู่บล็อก except เพื่อแสดงข้อความแทน

    print("\n===5===") ########################################################################
    # ประเภทของ Exception ในภาษา Python

    # Python มีประเภทของข้อผิดพลาด (Exception) หลายชนิด
    # ซึ่งสามารถศึกษารายละเอียดทั้งหมดได้จากเอกสารทางการที่:
    # 🔗 https://docs.python.org/3/library/exceptions.html

    # ตัวอย่างประเภทของ Exception ที่พบบ่อย

    # ประเภท Exception        ความหมาย
    # ArithmeticError         ข้อผิดพลาดที่เกิดจากการคำนวณทางคณิตศาสตร์
    # └ FloatingPointError    เกิดจากการดำเนินการกับเลขทศนิยมที่ไม่ถูกต้อง
    # └ OverflowError         ผลลัพธ์ของการคำนวณมีค่ามากเกินกว่าที่สามารถจัดเก็บได้
    # └ ZeroDivisionError     เกิดจากการหารด้วยศูนย์
    # NameError               ไม่พบชื่อตัวแปรที่เรียกใช้งาน
    # RuntimeError            ข้อผิดพลาดที่เกิดขึ้นระหว่างการรันโปรแกรมทั่วไป
    # SyntaxError             เขียนคำสั่งผิดไวยากรณ์ (เช่น ลืมวงเล็บ ลืมโคลอน :)
    # TypeError               ใช้ชนิดข้อมูลผิด เช่น บวกเลขกับข้อความ
    # ValueError              ค่าไม่ถูกต้องตามชนิดข้อมูลที่กำหนด เช่น แปลงข้อความที่ไม่ใช่ตัวเลขเป็น int
    # IndexError              เข้าถึงตำแหน่งของลิสต์ที่อยู่นอกขอบเขต
    # KeyError                จับข้อผิดพลาดกรณีใช้ key ที่ไม่มีใน dictionary
    # FileNotFoundError       หากเกิดข้อผิดพลาดว่าไม่พบไฟล์


    print("\n===6===") ##########################################################################
    # print("\n===6===")  # แสดงหัวข้อหรือแบ่งส่วนของโปรแกรมด้วยข้อความ "===6==="
    #
    # try:
    #     num1 = int(input("Enter value number1 : "))  # รับค่าตัวเลขแรกจากผู้ใช้ และแปลงเป็น int
    #     num2 = int(input("Enter value number2 : "))  # รับค่าตัวเลขที่สองจากผู้ใช้ และแปลงเป็น int
    #     print("number1 + number2 = ", num1 + num2)  # แสดงผลรวมของ num1 และ num2
    #     print("number1 - number2 = ", num1 - num2)  # แสดงผลลบของ num1 และ num2
    #     print("number1 * number2 = ", num1 * num2)  # แสดงผลคูณของ num1 และ num2
    #     print("number1 / number2 = ", num1 / num2)  # แสดงผลหารของ num1 และ num2
    #
    # except ValueError:  # ดักจับกรณีผู้ใช้ป้อนข้อมูลที่ไม่สามารถแปลงเป็น int ได้
    #     print("You input data in correct, input again.")  # แจ้งว่าข้อมูลไม่ถูกต้อง ให้ป้อนใหม่
    #
    # except ZeroDivisionError:  # ดักจับกรณีที่ num2 เป็น 0 แล้วนำไปหาร
    #     print("Number is not divide with zero.")  # แจ้งว่าไม่สามารถหารด้วยศูนย์ได้
    #
    # except NameError:  # ดักจับกรณีที่ใช้ตัวแปรที่ยังไม่ได้ประกาศ
    #     print("Use variable not define.")  # แจ้งว่ามีการใช้ตัวแปรที่ยังไม่ได้กำหนด
    #
    # except:  # ดักจับข้อผิดพลาดอื่น ๆ ที่ไม่อยู่ในกลุ่มด้านบน
    #     print("Error in program.")  # แจ้งว่าเกิดข้อผิดพลาดในโปรแกรม
    #
    # print("This is test Exception")  # แสดงข้อความเพื่อยืนยันว่าโปรแกรมยังคงทำงานต่อหลังจากการดักจับข้อผิดพลาด

    # try:
    #     num1 = int(input("Enter value number1 : "))
    #     num2 = int(input("Enter value number2 : "))
    #     print("number1 + number2 = ", num1+num2)
    #     print("number1 - number2 = ", num1-num2)
    #     print("number1 * number2 = ", num1*num2)
    #     print("number1 / number2 = ", num1/num2)
    # except ValueError:  # ValueError  ค่าไม่ถูกต้องตามชนิดข้อมูลที่กำหนด เช่น แปลงข้อความที่ไม่ใช่ตัวเลขเป็น int
    #     print("You input data in correct, input again.")
    # except ZeroDivisionError: # └ ZeroDivisionError เกิดจากการหารด้วยศูนย์
    #     print("Number is not divide with zero.")
    # except NameError: # NameError ไม่พบชื่อตัวแปรที่เรียกใช้งาน
    #     print("Use variable not define.")
    # except: # ดักจับข้อผิดพลาดอื่น ๆ ที่ไม่อยู่ในกลุ่มด้านบน
    #     print("Error in program.")
    # print("This is test Exception")

    #ทำไว้ show ใน terminal
    count = 0
    while count <= 3:
        try:
            num1 = [20,30,20]
            num2 = [10,0,"10S"]
            num1 = num1[count]
            num2 = num2[count]
            print(f"Enter value number1 : {num1}")
            print(f"Enter value number2 : {num2}")
            print("number1 + number2 = ", num1+num2)
            print("number1 - number2 = ", num1-num2)
            print("number1 * number2 = ", num1*num2)
            print("number1 / number2 = ", num1/num2)
        except ValueError:  # ValueError  ค่าไม่ถูกต้องตามชนิดข้อมูลที่กำหนด เช่น แปลงข้อความที่ไม่ใช่ตัวเลขเป็น int
            print("You input data in correct, input again.")
        except ZeroDivisionError: # └ ZeroDivisionError เกิดจากการหารด้วยศูนย์
            print("Number is not divide with zero.")
        except NameError: # NameError ไม่พบชื่อตัวแปรที่เรียกใช้งาน
            print("Use variable not define.")
        except: # ดักจับข้อผิดพลาดอื่น ๆ ที่ไม่อยู่ในกลุ่มด้านบน
            print("Error in program.")
        print("This is test Exception")
        print()
        count += 1

    print("\n===8===") #######################################################################################
    # try:
    #     num_dict = {1: "one", 2: "two", 3: "three"}  # สร้าง dictionary ที่มี key เป็น 1, 2, 3
    #     num_list = [1, 2, 3]  # สร้าง list ที่มีสมาชิกเป็น 1, 2, 3
    #
    #     for n in range(len(num_list)):  # วนลูปตามจำนวนสมาชิกของ list
    #         print(num_list[n])  # แสดงค่าที่ตำแหน่ง index n ของ list
    #
    #     for n in range(len(num_dict)):  # วนลูปตามจำนวนสมาชิกของ dict (คือ 3 รอบ: n = 0, 1, 2)
    #         print(num_dict[n])  # จะเกิด KeyError เพราะ dict นี้ไม่มี key = 0 (มีแค่ 1, 2, 3)
    #
    # except KeyError:  # จับข้อผิดพลาดกรณีใช้ key ที่ไม่มีใน dictionary
    #     print("Your use key not found.")  # แสดงข้อความเมื่อเกิด KeyError
    #
    # except IndexError:  # จับข้อผิดพลาดกรณีเข้าถึง index ที่ไม่อยู่ใน list
    #     print("You define index error.")  # แสดงข้อความเมื่อเกิด IndexError
    #
    # print("This is test use exception.")  # แสดงข้อความท้ายโปรแกรม ไม่ว่าจะเกิดข้อผิดพลาดหรือไม่

    try:
        num_dict = {1:"one",2:"two",3:"three"}
        num_list = [1,2,3]

        for n in range(len(num_list)):
            print(num_list[n])
        for n in range(1, 4):
            print(num_dict[n])
        for n in num_dict:
            print(num_dict[n])
        for n in range(len(num_dict)): # ผิดผลาด เพระ len มีค่า 3 จะเริ่มที่ 0,1,2 ซึ่ง dict นี้ key เริ่มที่ 1 - 3
            print(num_dict[n])
    except KeyError: # จับข้อผิดพลาดกรณีใช้ key ที่ไม่มีใน dictionary
        print("Your use key not found.")
    except IndexError:  # IndexError เข้าถึงตำแหน่งของลิสต์ที่อยู่นอกขอบเขต
        print("You define index error.")
    print("This is test use exception.")

    print("\n===10===")
    # การใช้ try-except-else เป็นการครอบส่วนของโปรแกรมที่อาจเกิดข้อผิดพลาดขึ้น
    # หากมีข้อผิดพลาด โปรแกรมจะไปทำงานในส่วนของ except
    # แต่ถ้าไม่เกิดข้อผิดพลาด โปรแกรมจะไปทำงานในส่วนของ else แทน

    # โครงสร้าง:
    # try:
    #     # คำสั่งที่อาจเกิดข้อผิดพลาด
    # except ชนิดของข้อผิดพลาด:
    #     # คำสั่งเมื่อเกิดข้อผิดพลาด
    # else:
    #     # คำสั่งที่จะทำเมื่อไม่เกิดข้อผิดพลาด

    # ตัวอย่าง:
    # try:
    #     number = int(input("ป้อนตัวเลข: "))
    # except ValueError:
    #     print("กรุณาป้อนเป็นตัวเลขเท่านั้น")
    # else:
    #     print(f"คุณป้อนเลข {number} ซึ่งถูกต้องแล้ว")

    print("\n===11===") ###############################################################################

    # การใช้ try-except-finally เป็นการครอบส่วนของโปรแกรมที่อาจเกิดข้อผิดพลาดขึ้น
    # หากเกิดข้อผิดพลาด โปรแกรมจะไปทำงานในส่วนของ except
    # แต่ไม่ว่าจะเกิดหรือไม่เกิดข้อผิดพลาด ส่วนของ finally จะทำงานเสมอ

    # โครงสร้าง:
    # try:
    #     # คำสั่งที่อาจเกิดข้อผิดพลาด
    # except ชนิดของข้อผิดพลาด:
    #     # คำสั่งเมื่อเกิดข้อผิดพลาด
    # finally:
    #     # คำสั่งที่จะทำเสมอ ไม่ว่าจะเกิดหรือไม่เกิดข้อผิดพลาด

    # ตัวอย่าง:
    # try:
    #     number = int(input("ป้อนตัวเลข: "))
    #     result = 10 / number
    #     print("ผลลัพธ์:", result)
    # except ZeroDivisionError:
    #     print("ไม่สามารถหารด้วยศูนย์ได้")
    # except ValueError:
    #     print("กรุณาป้อนตัวเลขเท่านั้น")
    # finally:
    #     print("จบกระบวนการคำนวณ")

    print("\n===12===") ###############################################################################
    # try:
    #     filename = input("Enter file name : ")  # รับชื่อไฟล์จากผู้ใช้
    #     fin = open(filename, encoding="utf-8")  # พยายามเปิดไฟล์ด้วย encoding แบบ UTF-8
    #     data = fin.read()  # อ่านข้อมูลทั้งหมดจากไฟล์
    #     print(data)  # แสดงข้อมูลที่อ่านได้
    #     fin.close()  # ปิดไฟล์
    # except FileNotFoundError:  # หากเกิดข้อผิดพลาดว่าไม่พบไฟล์
    #     print(f"File {filename} not open, this file not found.")  # แสดงข้อความว่าไม่พบไฟล์
    # else:  # ถ้าไม่มีข้อผิดพลาดเกิดขึ้น
    #     print("Work Complete.")  # แสดงข้อความว่างานสำเร็จแล้ว
    # finally:
    #     print("End program.")  # แสดงข้อความตอนจบ ไม่ว่าจะเกิดหรือไม่เกิดข้อผิดพลาด


    # try:
    #     filename = input("Enter file name : ")
    #     fin = open(filename, encoding="utf-8")
    #     data = fin.read() # อ่านข้อมูลทั้งหมดจากไฟล์
    #     print(data)
    #     fin.close()
    # except FileNotFoundError: # หากเกิดข้อผิดพลาดว่าไม่พบไฟล์
    #     print(f"File {filename} not open, this file not found.")
    # else: # ถ้าไม่มีข้อผิดพลาดเกิดขึ้น
    #     print("Work Complete.")
    # finally:  # แสดงข้อความตอนจบ ไม่ว่าจะเกิดหรือไม่เกิดข้อผิดพลาด
    #     print("End program.")


    # ทำไว้ show ใน terminal
    count = 0
    while count <= 1:
        try:
            filename = ["mydata.txt","notnot"]
            filename = filename[count]
            print(f"Enter file name : {filename}")
            fin = open(filename, encoding="utf-8")
            data = fin.read() # อ่านข้อมูลทั้งหมดจากไฟล์
            print(data)
            fin.close()
        except FileNotFoundError: # หากเกิดข้อผิดพลาดว่าไม่พบไฟล์
            print(f"File {filename} not open, this file not found.")
        else: # ถ้าไม่มีข้อผิดพลาดเกิดขึ้น
            print("Work Complete.")
        finally:  # แสดงข้อความตอนจบ ไม่ว่าจะเกิดหรือไม่เกิดข้อผิดพลาด
            print("End program.")
        print()
        count += 1

    print("\n===14===") ###############################################################################
    from w7.ModuleProduct import read_product,add_product,report_product,report_from_file

    DATAFILE = "product.txt"

    def main():
        menu = ("=" * 17) + "\n| Product Menu |\n" + ("=" * 17)
        menu += "\n1. Add Product\n2. Report Product from File\n"
        menu += "3. Report Product by Price\n"
        menu += "4. Exit\nEnter choice : "
        while True:
            choice = input(menu)
            if choice == "1":
                add_product(DATAFILE)
            elif choice == "2":
                report_from_file(DATAFILE)
            elif choice == "3":
                products = read_product(DATAFILE)
                report_product(products)
            elif choice == "4":
                print("Exit Program")
                break
            else:
                print("No choice, input again.")

    if __name__ == "__main__":
        main()

if __name__ == "__main__":
    s()