from fileinput import close


def input_subject():
    subject = int(input("กรอกรหัสรายวิชา : "))
    print("เพิ่มข้อมูลรายวิชาเสร็จสิ้น\n")
    main()
def input_std():
    std = int(input("กรอกรหัสนักศึกษา : "))
    print("เพิ่มข้อมูลนักศึกษาเสร็จสิ้น\n")
    main()
# def report_subject():
#
# def report_gpa():

def main():
    print("1.จัดเก็บข้อมูลรายวิชา")
    print("2.จัดเก็บข้อมูลนักศึกษา")
    print("3.ออกรายงานการลงทะเบียนเรียนรายวิชา")
    print("4.ออกรายงานผลเกรดเฉลี่ย")
    print("5.ปิดโปรแกรม")
    choice = int(input("เลือกรายการ : "))
    if choice == 1:
        return input_subject()
    elif choice == 2:
        return input_std()
    else:
        close()

    # with open(f"{std}.txt","w") as file:
    #     file.write(f"|{std}|{subject}")
main()