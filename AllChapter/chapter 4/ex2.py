# from random import uniform
# uniform1 = round(uniform(30,50),2) #ใช้ uniform เพื่อหาค่าสุ่มตัวเลขที่มีทศนิยม แล้วใช้ round เพื่อกำหนดทศนิยม 2 ตำแหน่ง
# uniform2 = round(uniform(30,50),2) #ต้องสร้างหลายตัวเพราะสุ่มหลายค่า
# uniform3 = round(uniform(30,50),2)
# uniform4 = round(uniform(30,50),2)
# uniform5 = round(uniform(30,50),2)
# total = round(uniform1 + uniform2 + uniform3 + uniform4 + uniform5,2)
# print("Value random :",uniform1,",",uniform2,",",uniform3,",",uniform4,",",uniform5)
# print("Total value :",total)
# print("Average value :",round((total / 5),2))

from random import uniform
total,strinput = 0.0,""
for n in range(1,6):
    num = round(uniform(30,50),2)
    total += num 
    strinput += str(num) + " , "
    
print("Value random :", strinput)
print("Total value :",round(total,2))
print("Average :", round(total/n,2))

# from random import uniform 
# total = 0
# print("Value random : ",end="")
# for _ in range(5):
#     rd = round(uniform(30,50),2)
#     total += rd
#     print(f"{rd} , " if _ < 4 else f"{rd}",end="")
# print(f"\nTotal value : {round(total,2)}\nAverage value : {round(total / 5,2)}")