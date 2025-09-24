def add_employee(filename):
    print("Enter data employee.")
    emp_id = input("Input employee id : ")
    emp_name = input("Input employee name : ")
    emp_surname = input("Input employee surname : ")
    emp_salary = input("Input employee salary : ")
    fout = open(filename,"a",encoding="UTF_8")
    fout.write(emp_id+","+emp_name+","+emp_surname+","+emp_salary+"\n")
    fout.close()
    print("Save Data Employee allready.\n")

def read_file(filename):
    with open(filename) as fin:
        for data in fin:
            print(data)

def read_to_memory(filename):
    datas = []
    with open(filename) as fin:
        for data in fin:
            data = data.rstrip("\n") #.rstrip() ใช้เพื่อลบอักขระด้านขวาสุดของสตริง   (ถอด)
            datas.append(data.split(",")) #.split() ช่วยแยกข้อความออกเป็นรายการ  (แยก)
    return(datas)

def report_employee(datas):
    head = "Report Employee".center(50) + "\n" #.center() ใช้สำหรับ จัดตำแหน่งสตริงให้อยู่ตรงกลาง
    head += ("-" * 50) + "\n"
    head += "| No.|  Id  |  Name     | Surname     |  Salary  |\n"
    head += ("-" * 50 + "\n")
    n = 1
    mess = ("")
    for data in datas:
        mess += f"|{n:3} | {data[0]:^5} |{data[1]:^10} |{data[2]:^12} |" #^: จัดข้อความ ให้อยู่กลาง
        mess += format(float(data[3]), ",.2f").rjust(10) + "|\n" #.rjust() ใช้สำหรับ จัดข้อความให้อยู่ชิดขวา
        n += 1
    print(head, end="")
    print(mess, end="")
    print(("-" * 50) + "\n")

filename = "employee.txt"
add_employee(filename)
read_file(filename)
data = read_to_memory(filename)
print(data)
report_employee(data)