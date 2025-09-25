print("===14===")
print("Hello")
print( 123)
print( 2.3)
print()
print("Pythong", 3, ".12.3")

print("\n===15===")
print("Hello","Somchai",sep=",") #sep = , กำหนดค่าเว้นว่าง
print(123, 2.3,sep=",",end="\n\n")
version = 3.12
print("Python", version, end="") #end = กำหนดค่าการขึ้นบรรทัดใหม่
print(".4")

print("\n===16===")
print("Sum is result of adding two numbers, for example, "#\
      "1 + 1 is ", 1+1) # \ แบ่งบรรทัด(ไม่ค่อยจำเป็น)

print("\n===Ex29===")
# rows = 5
# for i in range(1, rows):
#     for j in range(1, i + 1):
#         print("* ", end="")
#     print("\r")

#------------
# rows = 5
# for j in range(1, rows + 1): #ตั้งแต่ 1 ถึง 5 (รวม 5)
#     print("* " * j)
#------------

rows = 5
for j in range(1, rows + 1):
    print("  " * (rows - j) + "* " * j)

# for i in range(5, 0 ,-1): #ตั้งแต่ 5 ไป 0 (รวม 0)
#     print("* " * i)  # str * จำนวน

Id = input("\nId : ")
name = input("English Name : ")
t_name = input("Thai Name : ")
n_name = input("Nick Name : ")
sex = input("Sex : ")
age =input("Age : ")

print("\nId : ", Id)
print("English Name : ", name)
print("Thai Name : ", t_name)
print("Nick Name : ", n_name)
print("Sex : ", sex)
print("Age : ", age)