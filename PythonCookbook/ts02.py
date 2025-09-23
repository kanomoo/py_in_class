import time
print("===========32===========".center(72))####################################################################

# print(1,end="\r") # \r ใช้เพื่อให้ พิมพ์ทับบนบรรทัดเดิม
# time.sleep(1)
# print("two",end="\r")
# time.sleep(1) # หน่วงเวลาเป็นวินาที
# print("สาม",end="\r")
# time.sleep(1) # หน่วงเวลาเป็นวินาที
#
#
# print("Loading...", end="\r")
# time.sleep(1)
# print("Done!     ", end="\r")
# time.sleep(1)
# print(" " * 10, end="\r")

# print(1,end="\r")
# time.sleep(1)
# print(" " * 10, end="\r")
# print("two", end="\r")
# time.sleep(1)
# print(" " * 10, end="\r")
# print("สาม", end="\r")

# data = [1,"two","สาม"]
# for d in data:
#     print(d, end="\r")
#     time.sleep(1)
#     print(" " * 10, end="\r")


# print("\n",end="")
#
# for i in range(10,0,-1):
#     print("รอ", i, "วินาที", end="\r")
#     time.sleep(1)
#     print(" " * 50,end="\r")
#
#     if i == 1:print("เริ่มการดาวน์โหลด", end="\n\n")
######################################################################################
# for i in range(10):
#     print(f"รอ {i+1} วินาที", end="\r", flush=True)
#     time.sleep(1)
# print("เริ่มการดาวโหลด")
###################################################################################################
print("เอา comment ออกเอาเกี่ยวกับการปริ้นบรรทัดเดิม กับ time sleep")
print("===========35===========".center(72))####################################################################

# f-string
n,a = "สมชาย", 40
print(f"ผมชื่อ {n} ปัจจุบัน {a} ปี")
ndigit = 2
print(f"{123.4567:.{ndigit}f}")

print("===========36===========".  center(72))####################################################################

import random
print()
pi = 3.14
radius = random.randint(10,20)

c_area = pi * (radius ** 2 )
c_pmt = 2 * pi * radius

str = f"วงกลมที่มีรัศมี: {radius} \n"
str += f"มีพื้นที่: {c_area:.2f} เส้นรอบวง: {c_pmt:.2f}\n"
print(str)

width = random.randint(100, 1500)
height = random.randint(100, 1500)

r_area = width * height
r_pmt = (2 * width) + (2 *height)
str = f"สี่เหลี่ยมมุมฉากที่กว้าง: {width:,} สูง: {height:,}\n"
str += f"มี่พีื้นทที่: {r_area:,} เส้นรอบรูป: {r_pmt:,}"
print(str, "\n")

print("===========37===========".center(72))####################################################################

a, b = 10, 20
print(f"{a} + {b} = {a + b}")

y_b = 1995
y_c = 2025
print(f"เขาเกิดปี {y_b} ปัจจุบันปี {y_c} ดังนั้นเขามีอายุ {y_c - y_b}")

y = 2568
print(f"ปัจจุบันปีพ.ศ. {y} หรือค.ศ. {y - 543}")

n = 108
print(f"\n{n} เป็นเลข {"คู่" if n % 2 == 0 else "คี่"}")

print("===========38===========".center(72))####################################################################

import  random
print()
pi = 3.14
r = random.randint(10,20)
str = f"วงกลมที่มีรัศมี {r} \n"
str += f"มีพื้นที่: {pi * (r**2):.2f} เส้นรอบวง: {2*pi*r:.2f}\n"
print(str)

w = random.randint(100,1500)
h = random.randint(100,1500)
str = f"สี่เหลี่ยมมุมฉากที่กว้าง: {w:,} สูง: {h:,}\n"
str += f"มีพืื้นที: {w * h:,} เส้นรอบรูป: {2*w + 2*h:,}"
print(str,"\n")

print(f"{"Python":7}{970:5}")

print("===========39===========".center(72))####################################################################
id = 123
name = "iPhone"
price = 35000
sp = " " * 2 #จำนว่องว่างคั่นระหว่างคอลัมน์
print(f"{id:<4}{sp}{name:9}{sp}{price:<6}")
print(f"{101:<5}{" " * 3}{"Python":15}{" "*3}{1500:6}")
print(f"{102:<5}{" " * 3}{"cobra":15}{" "*3}{990:6}")