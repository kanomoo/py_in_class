from fontTools.varLib.plot import stops
from pandas.core.methods.selectn import SelectNSeries

print("===========18===========".center(72))####################################################################

from random import randint
l_word = ["ศูนย์" ,"หนึ่ง", "สอง", "สาม", "สี่", "ห้า" ]
r = randint(0,10)
try: word = l_word[r]
except: print("Error เลขลำดับเกินขอบเขตของลิสต์")
else: print(f"{r} อ่านว่า {word}")
finally: print(f"เลขที่สุ่มได้คือ: {r}")
########################################################################
# def remove_list(lst, value):
#     #การลบสมาชิกของลิสต์ หากเราระบุสมาชิกที่ไม่มีอยู่ในลิสต์จะเกิดข้อผิดพลาด
#     #ดังนั้นจึงกำหนดขั้นตอบการลบไว้ในบล็อก try
#     #แต่ไม่ว่าการลบจะสำเร็จหรือไม่ ก็จะคืนค่าลิสต์ผลลัพธ์กลับออกไปเสมอ       *******************
#     try: lst.remove(value)
#     finally: return lst
#
# number_words = ["zero", "one", "two", "three", "four", "five"]
# a = remove_list(number_words,"ten")
# print(*a,sep=", ")
#
# a = remove_list(number_words, "one")
# print(*a,sep=", ")
print("########################################################################")
def remove_list(lst, value):
    try: lst.remove(value)   # แต่ไม่ว่าการลบจะสำเร็จหรือไม่ ก็จะคืนค่าลิสต์ผลลัพธ์กลับออกไปเสมอ
    finally: return lst # finally คือโค้ดที่ จะทำแน่นอน ไม่ว่าจะเกิดข้อผิดพลาดหรือไม่

l_word = ["zero","one","two","three","four","five"]
a = remove_list(l_word,"one")
print(*a,sep=", ")
# *a คือการ "แตกค่าทุกตัวในลิสต์ a อvอกมา" แล้วส่งต่อเข้า print() ทีละตัว โดยไม่ต้องใช้ลูปเอง

a = remove_list(l_word, " ") #.ใส่ try ไว้ไม่ว่ายังไงก็คืนค่า lst
print(*a,sep=", ")

print("===========19===========".center(72))####################################################################

# x = -1
# if x < 0: raise Exception("ข้อมูลเป็นจำนวนลบ") # raise เป็นการสั่งให้แสดงข้อผิดพลาด

# try :
#     x =  1
#     if x < 0: raise Exception("ข้อมูลเป็นจำนวนลบ") #ข้อผิลพลาดตรงนี้
# except Exception as err: print(err)
# else print("ข้อมูลเป็นจำนวนบวก")

try:
    x = -1
    if x < 0: raise Exception("ข้อมูลเป็นจำนวนลบ") #ใช้ try raise จะไม่ทำงานเลยต้องกำหนดใน except
except Exception as err: print(err)
else: print("ข้อมูลเป็นจำนวนบวก")
finally: print("ขอบคุณครับ")
########################################################################

print("===========20===========".center(72))####################################################################

try:
    # a = int(input("ใส่เลขจำนวนเต็มที่มากกว่า 0 >> "))
    a = -1
    assert a > 0, "ต้องกำหนดค่ามากกว่า 0" # assert เป็นการระบุเงื่อนไขที่จะไม่เกิดข้อผิดพลาด
except Exception as err: print(err)
else: print("กำหนดค่าถูกต้อง")
print()
########################################################################
# def func():
#     value = input("กำหนดเลขจำนวนเต็ม 1 - 100 >> ")
#     if not value.isdigit(): #สตริง (string) ที่อยู่ในตัวแปร value มีแต่ ตัวเลขทั้งหมด (0–9) หรือไม่
#         raise Exception("ต้องกำหนดข้อมูลเป็นจำนวนเต็มบวก")
#     assert int(value) <= 100 and int(value) >= 0,"ต้องกำหนดค่าระหว่าง 1 - 100"
#     return value
# try: result = func()
# except Exception as err: print(err)
# else: print("ค่าที่กำหนดคือ:",result)

def func():
    # value = input("กำหนดจำนวนเต็ม 1 - 100 >> ")
    value = "10"
    if not value.isdigit(): raise Exception("ต้องกำหนดตัวเลขเป็นจำนวนเต็ม")
    assert int(value) >= 0 and int(value) <= 100,"ต้องกำหนดจำนวนเต็ม 1 - 100"
    return value
try: value = func()
except Exception as err: print(err)
else: print(f"ค่าของจำนวนคือ : {value}")

# try:
#     num = int(input("กำหนดเลขจำนวนบวก 1-100 >> "))
#     if num < 0: raise Exception("ต้องกำหนดข้อมูลเป็นเลขจำนวนเต็มบวก")
#     assert num <= 100 and num >= 1 , "ต้องกำหนดค่าระหหว่าง 1 - 100"
# except Exception as err:print(err)
# else: print(f"ค่าที่เหลือคือ: {num}")

print("===========21===========".center(72))####################################################################

a = 12
if type(a) is int: print(True)
if type(a).__name__ == "int": print(True) #.__name__ เปรียนเทียบโดยเขียนชนิดข้อมูลในแบบสตริง
if isinstance(a,int): print(True)
print("########################################################################")
a = 123
b = -4.56
c = True

print("===========23===========".center(72))####################################################################

a = eval("123") # eval แปลง string เป็นชนิดที่สอดคล้องกับค่ากี่กำหนด
b = eval("[1,2,3]")
print(type(a).__name__,type(b).__name__)
print(a,b,sep="  ")

print("===========24===========".center(72))####################################################################

try:
    # num = input("ใส่จำนวนเต็มหรือทศนิยม >> ")
    num = "-3.14" # ต้องรับค่าเป็น string ก่อน
    assert type(eval(num)) == float,"ต้องใส่เลขจำนวนหรือทศนิยมเท่านั้น" # eval แปลง string เป็นชนิดที่สอดคล้องกับค่ากี่กำหนด
except Exception as err: print(err)
else: print("ขอบคุณครับ")

print("===========25===========".center(72))####################################################################

x = 10
# if x % 2 ==0: print("เลขคู่") แบบปกติ
# else: print("เลขคี่")

# การเขียน if else แบบบรรทัดเดียว
y = 0
z = x / y if y != 0 else print("ตัวหารเป็น 0 ไม่ได้")

print("เลขคู่") if x % 2 == 0 else print("เลขคี่")
print("เลขคู่" if x % 2 == 0 else "เลขคี่")

s = "OK" if a > 0 else "Error"
print(s)

print("===========26===========".center(72))####################################################################

import random
balance = random.randint(1000, 10000)
amount = random.randint(-100, 15000)
balance -= amount if amount in range(1, balance) else 0
print(balance)

# ใช้รูปแบบ for-else และ while-else แบบมีเงื่อนไข
sum = 0
for i in range(11):
    sum += i
else: print(f"sum = {sum}")
# แต่ถ้าเป็นแบบนี้ else จะไม่ทำงาน
for i in range(11):
    sum += i if sum != 6 else None
print()
# x = input("ใส่จำนวนเต็มบวกเท่านั้น >> ")
# found_non_digit = False
# i = 0
# while i < len(x):
#     if not x[i].isdigit():
#         found_non_digit = True
#         print("ใส่ค่าไม่ตรงเงื่อนไข")
#         break
#     i += 1
# else: print("ใส่ค่าได้ถูกต้อง")

# name = input("ใส่จำนวนเต็มบวกเท่านั้น >> ")
name = "-1"
print("ใส่ค่าได้ถูกต้อง" if name.isdigit() else "ใส่ค่าไม่ตรงเงื่อนไข")

print("===========27===========".center(72))####################################################################

# ใช้ match-case ทดแทน switch-case

# size = input("enter size (s, m, l) >> ")
size = "s"
print(f"enter size (s, m, l) >> {size}")
match size:
    case "s": print("small")
    case "m": print("medium")
    case "l": print("large")
    case _: print("error")

# ถ้ามีหลายค่าที่จะดำเนินการแบบเดียวกัน
# m = int(input("ลำดับของเดือนในรอบปี (1-12) >> "))
m = 12
print(f"ลำดับของเดือนในรอบปี (1-12) >> {m}")
num_days = 0
match m:
    case 1 | 3 | 5 | 7| 8 | 10 | 12: num_days = 31
    case 4 | 6 | 9 | 11: num_days = 30
    case _: num_days = -1
print(num_days)
print("####################################################################")

# ตรวจสอบไฟล์ที่รันด้วย if__name__ == "__main__" | __name__ จะเป็น __main__ ถ้าเรียกว่าไฟล์นี้ขึ้นมาทำงานโดยตรง
print(__name__)
import app
app.run(),app.func()

print("===========29===========".center(72))####################################################################
