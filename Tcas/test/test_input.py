
def menu_main(): # report main menu
    head = f"|{"TCAS System":^25}|"
    line = f"+{"=" * (len(head) - 2)}+"
    choice = input(f"{line}\n{head}\n{line}\n|{"1. Course information":25}|\n{line}\nSelect option : ")
    match choice:
        case "1":
            course_info()

def data_course_info():
    data = []
    with open(r"Tcas\test\course_info.txt","r") as fout:
        for i in fout: 
            data.append(i.strip("\n").split("|"))
    return(data)

def course_info():
    head = f"|{"Course information":^30}|"
    line = f"+{"-" * (len(head) - 2)}+"
    choice = input(f"{line}\n{head}\n{line}\n|{"1. Add Course Information":{len(head)-2}}|\n|{"2. Report Course Information":{len(head)-2}}|\n{line}\nSelect option : ")
    match choice:
        case "1":
            add_course_info()
        case "2": 
            report_course_info()

def add_course_info():
    with open(r"Tcas\test\course_info.txt","a") as fin:
        # institutional =  input("กรุณากรอกชื่อสถานบัน")
        # c_name = input("กรุณากรอกหลักสูตร : ")
        # eng_c_name = input("กรุณากรอกชื่อหลักสูตรภาษาอังกฤษ : ")
        # faculty = input("กรุณากรอกชื่อคณะ")
        # c_type = input("กรุณากรอกประเภทหลักสูตร : ")
        # campus = input("กรุณากรอกวิทยาเขต : ")
        # expenses = input("กรุณากรอกค่าใช้จ่ายต่อภาคเรียน : ")
        # employment_rate = input("กรุณากรอกอัตราการได้งานทำ : ")
        # median_salary = input("กรุณากรอกค่ามัธยฐานเงินเดือน : ")

        institutional =  "มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ"
        faculty = "คณะเทคโนโลยีและการจัดการอุตสาหกรรม"
        c_name = "วท.บ.เทคโนโลยีสารสนเทศ (ภาษาไทย ปกติ) วิทยาเขต ปราจีนบุรี"
        eng_c_name = "Bachelor of Science Program in Information Technology"
        c_type = "ภาษาไทย ปกติ"
        campus = "ปราจีนบุรี"
        expenses = "19,000 ต่อภาคเรียน"
        employment_rate = "ร้อยละ 74.84 (ภาพรวมคณะ รุ่นปีการศึกษา 2565)"
        median_salary = "19,340 บาท (ภาพรวมคณะ รุ่นปีการศึกษา 2565)"

        fin.writelines(("|".join((institutional,faculty,c_name,eng_c_name,c_type,campus,expenses,employment_rate,median_salary)))+"\n")

def report_course_info():
    data = data_course_info()
    head = f"|{"Report Course Infomation":^55}|"
    line = f"+{"-" * (len(head) - 2)}+"
    print(f"{line}\n{head}\n{line}")
    for i in data:

        for n in i:
            print(n)
        print(line)

def advavdai_report():
    pass


def main():
    # course_info()
    report_course_info()

    # add_course_info()
    # data_course_info()

    # menu_main()
if __name__ == "__main__":
    main()