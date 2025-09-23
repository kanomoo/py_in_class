import math

fnum = float(input("Enter float number : "))
print()
print("Ceil number :", math.ceil(fnum))
print("Floor number :", math.floor(fnum))
print("Sqrut number :", round(math.sqrt(fnum),6))
print("Trunc number :", math.trunc(fnum))
print()

num = math.trunc(fnum)
print("Degree Angle :", num)
print("Radians Angle:", round(math.radians(num),6))
print("sin  : ", round(math.sin(math.radians(num)),6))
print("cos  : ", round(math.cos(math.radians(num)),6))
print("tan  : ", round(math.tan(math.radians(num)),6))