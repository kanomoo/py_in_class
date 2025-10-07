from wcwidth import wcswidth
# คำนวณความกว้างของการแสดงผล

def pad_text(text, width): # padding text เติมช่องว่าง ใช้เฉพาะภาษาไทย
    real_width = wcswidth(text)                         # คำนวณความกว้างจริงของข้อความในเทอมินอล (นับช่องว่างที่ข้อความใช้)
    if real_width < width:                              # ถ้าความกว้างจริงของข้อความน้อยกว่าความกว้างที่ต้องการ
        return text + " " * (width - real_width)        # เติมช่องว่างให้ครบตามความกว้างที่กำหนด เพื่อจัดข้อความให้อยู่ในตำแหน่ง len จริงๆ
    return text                                         # ถ้าความกว้างของข้อความมากกว่าหรือเท่ากับที่ต้องการ return เหมือนเดิม ใช้ format string จัดการต่อเอา

def menu_main(): # report main menu
    head = f"|{"TCAS System":^25}|"
    line = f"+{"=" * (len(head) - 2)}+"
    choice = input(f"{line}\n{head}\n{line}\n|{"1. Course information":25}|\n|{"2. Exit Program":25}|\n{line}\nSelect option : ")
    match choice:
        case "1":
            course_info()
        case "2":
            exit()

def data_course_info(): # เก็บข้อมูลจากไฟล์
    data = []
    with open(r"Tcas\test\course_info.txt","r") as fout:
        for i in fout: 
            data.append(i.strip("\n").split("|"))
    return(data)

def course_info(): # menu input course_info
    head = f"|{"Course information":^30}|"
    line = f"+{"-" * (len(head) - 2)}+"
    choice = input(f"{line}\n{head}\n{line}\n|{"1. Add Course Information":{len(head)-2}}|\n|{"2. Report Course Information":{len(head)-2}}|\n|{"3. Back to main":{len(head)-2}}|\n{line}\nSelect option : ")
    match choice:
        case "1":
            add_course_info()
        case "2": 
            report_course_info()
        case "3":
            back_to_main()

def add_course_info():
    with open(r"Tcas\test\course_info.txt","w") as fin:
        # institutional =  input("กรุณากรอกชื่อสถานบัน")
        # faculty = input("กรุณากรอกชื่อคณะ")
        # c_name = input("กรุณากรอกหลักสูตร : ")
        # eng_c_name = input("กรุณากรอกชื่อหลักสูตรภาษาอังกฤษ : ")
        # c_type = input("กรุณากรอกประเภทหลักสูตร : ")
        # campus = input("กรุณากรอกวิทยาเขต : ")
        # expenses = input("กรุณากรอกค่าใช้จ่ายต่อภาคเรียน : ")
        # employment_rate = input("กรุณากรอกอัตราการได้งานทำ : ")
        # median_salary = input("กรุณากรอกค่ามัธยฐานเงินเดือน : ")
      

        #  ==================== True Use
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

        # ==========================

        data_universities = [
        ["มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ","คณะเทคโนโลยีและการจัดการอุตสาหกรรม","วท.บ.เทคโนโลยีสารสนเทศ (ภาษาไทย ปกติ) วิทยาเขต ปราจีนบุรี","Bachelor of Science Program in Information Technology","ภาษาไทย ปกติ","ปราจีนบุรี","19,000 ต่อภาคเรียน","ร้อยละ 74.84 (ภาพรวมคณะ รุ่นปีการศึกษา 2565)","19,340 บาท (ภาพรวมคณะ รุ่นปีการศึกษา 2565)"],
        ["มหาวิทยาลัยธรรมศาสตร์","คณะวิทยาศาสตร์และเทคโนโลยี","วท.บ.วิทยาการคอมพิวเตอร์","Bachelor of Science Program in Computer Science","ภาษาไทย ปกติ","รังสิต","20,000 ต่อภาคเรียน","ร้อยละ 80.50 (ภาพรวมคณะ รุ่นปีการศึกษา 2564)","21,500 บาท (ภาพรวมคณะ รุ่นปีการศึกษา 2564)"],
        ["จุฬาลงกรณ์มหาวิทยาลัย","คณะวิทยาศาสตร์","วท.บ.เทคโนโลยีสารสนเทศ","Bachelor of Science Program in Information Technology","ภาษาไทย ปกติ","ปทุมวัน","22,000 ต่อภาคเรียน","ร้อยละ 78.00 (ภาพรวมคณะ รุ่นปีการศึกษา 2563)","23,300 บาท (ภาพรวมคณะ รุ่นปีการศึกษา 2563)"],
        ["มหาวิทยาลัยเกษตรศาสตร์","คณะวิทยาศาสตร์","วท.บ.เทคโนโลยีสารสนเทศ วิทยาเขตบางเขน","Bachelor of Science Program in Information Technology","ภาษาไทย ปกติ","บางเขน","18,500 ต่อภาคเรียน","ร้อยละ 76.20 (ภาพรวมคณะ รุ่นปีการศึกษา 2565)","19,800 บาท (ภาพรวมคณะ รุ่นปีการศึกษา 2565)"],
        ["มหาวิทยาลัยสงขลานครินทร์","คณะวิทยาศาสตร์","วท.บ.เทคโนโลยีสารสนเทศ","Bachelor of Science Program in Information Technology","ภาษาไทย ปกติ","หาดใหญ่","17,500 ต่อภาคเรียน","ร้อยละ 72.30 (ภาพรวมคณะ รุ่นปีการศึกษา 2564)","18,700 บาท (ภาพรวมคณะ รุ่นปีการศึกษา 2564)"],
        ["มหาวิทยาลัยขอนแก่น","คณะวิทยาศาสตร์","วท.บ.เทคโนโลยีสารสนเทศ","Bachelor of Science Program in Information Technology","ภาษาไทย ปกติ","เมืองขอนแก่น","16,800 ต่อภาคเรียน","ร้อยละ 74.10 (ภาพรวมคณะ รุ่นปีการศึกษา 2563)","17,900 บาท (ภาพรวมคณะ รุ่นปีการศึกษา 2563)"],
        ["มหาวิทยาลัยเชียงใหม่","คณะวิทยาศาสตร์","วท.บ.เทคโนโลยีสารสนเทศ","Bachelor of Science Program in Information Technology","ภาษาไทย ปกติ","เมืองเชียงใหม่","18,900 ต่อภาคเรียน","ร้อยละ 75.60 (ภาพรวมคณะ รุ่นปีการศึกษา 2565)","20,100 บาท (ภาพรวมคณะ รุ่นปีการศึกษา 2565)"],
        ["มหาวิทยาลัยมหิดล","คณะวิทยาศาสตร์","วท.บ.เทคโนโลยีสารสนเทศ","Bachelor of Science Program in Information Technology","ภาษาไทย ปกติ","พญาไท","21,800 ต่อภาคเรียน","ร้อยละ 79.90 (ภาพรวมคณะ รุ่นปีการศึกษา 2564)","22,900 บาท (ภาพรวมคณะ รุ่นปีการศึกษา 2564)"],
        ["มหาวิทยาลัยศรีนครินทรวิโรฒ","คณะวิทยาศาสตร์","วท.บ.เทคโนโลยีสารสนเทศ","Bachelor of Science Program in Information Technology","ภาษาไทย ปกติ","ประสานมิตร","19,300 ต่อภาคเรียน","ร้อยละ 73.40 (ภาพรวมคณะ รุ่นปีการศึกษา 2563)","20,500 บาท (ภาพรวมคณะ รุ่นปีการศึกษา 2563)"],
        ["มหาวิทยาลัยนเรศวร","คณะวิทยาศาสตร์","วท.บ.เทคโนโลยีสารสนเทศ","Bachelor of Science Program in Information Technology","ภาษาไทย ปกติ","เมืองพิษณุโลก","15,900 ต่อภาคเรียน","ร้อยละ 71.20 (ภาพรวมคณะ รุ่นปีการศึกษา 2565)","17,000 บาท (ภาพรวมคณะ รุ่นปีการศึกษา 2565)"],
        ["มหาวิทยาลัยบูรพา","คณะวิทยาศาสตร์","วท.บ.เทคโนโลยีสารสนเทศ","Bachelor of Science Program in Information Technology","ภาษาไทย ปกติ","เมืองชลบุรี","18,000 ต่อภาคเรียน","ร้อยละ 74.80 (ภาพรวมคณะ รุ่นปีการศึกษา 2564)","19,200 บาท (ภาพรวมคณะ รุ่นปีการศึกษา 2564)"],
        ["มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี","คณะเทคโนโลยีสารสนเทศ","วท.บ.เทคโนโลยีสารสนเทศ","Bachelor of Science Program in Information Technology","ภาษาไทย ปกติ","บางมด","20,500 ต่อภาคเรียน","ร้อยละ 77.90 (ภาพรวมคณะ รุ่นปีการศึกษา 2563)","21,700 บาท (ภาพรวมคณะ รุ่นปีการศึกษา 2563)"]    
        ]   
        for course in data_universities:
            course = "|".join(course)
            fin.write(course+"\n")

def report_course_info(): # report 
    head = f"|{"Report Course Infomation":^30}|"
    line = f"{"-" * len(head)}"
    choice = input(f"{line}\n{head}\n{line}\n|{"1. All Course Information":{len(head)-2}}|\n|{"2. Search Course Information":{len(head)-2}}|\n|{"3. Back to main":{len(head)-2}}|\n{line}\nSelect option : ")
    match choice:
        case "1":
            all_course_info()
        case "2": 
            search_course_info()
        case "3":
            back_to_main()

def all_course_info():
    result = ""
    datas = data_course_info()
    head = f"|{'Report Course Infomation':^90}|"
    line = "-" * len(head)
    # title = ["สถานบัน","คณะ","หลักสูตร","ชื่อหลักสูตรภาษาอังกฤษ","ประเภทหลักสูตร","วิทยาเขต","ค่าใช้จ่ายต่อภาคเรียน","อัตราการได้งานทำ","มัธยฐานเงินเดือน"]
    title = ["Institution","Faculty","Program","Program Name in English","Program Type","Campus","Tuition Fee per Semester","Employment Rate","Median Salary"]
    result += (f"{line}\n{head}\n{line}")
    for course in datas:
        for i in range(len(course)):
            col_data = pad_text(course[i], 90 - 29)  # ลบ len tile กับช่องว่างก่อน col_data
            result += (f"| {title[i]:25}| {col_data} |\n")
        result += line+"\n"
    print(result)

def search_course_info():
    head = f"|{'Report Course Infomation':^90}|"
    line = "-" * len(head)

def back_to_main():
    menu_main()

def main():
    # course_info()
    # report_course_info()

    # add_course_info()
    # data_course_info()

    # while True:
    #     menu_main()

    search_course_info()
    # all_course_info()
if __name__ == "__main__":
    main()