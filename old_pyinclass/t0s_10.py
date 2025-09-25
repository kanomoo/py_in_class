def s():
    print("===5===")  ##################################################
    # การเปิดไฟล์ในภาษา Python
    # การเปิดไฟล์ (open file) คือการสร้างการเชื่อมต่อระหว่าง โปรแกรม กับ ไฟล์ข้อมูล โดย# สามารถเปิดได้ 2 รูปแบบหลัก:
    # Input File: เพื่ออ่านข้อมูลจากไฟล์
    # Output File: เพื่อเขียนข้อมูลลงในไฟล์

    #________________________________________
    #  รูปแบบคำสั่ง
    #  fo = open(filename, mode='r', encoding=None)
    # fo	คือออบเจกต์ของไฟล์ที่ใช้เก็บข้อมูลหลังจากเปิด
    # filename	ชื่อไฟล์และเส้นทางที่จัดเก็บไฟล์ เช่น "data.txt"
    # mode	โหมดการทำงานของไฟล์ เช่น 'r', 'w', 'a'
    # encoding	การเข้ารหัสข้อมูลของไฟล์ (ใช้กับไฟล์ข้อความ เช่น "utf-8")

    #________________________________________
    #  ตัวอย่างโหมด (mode) ที่ใช้บ่อย
    # 'r'	อ่านไฟล์ (read)
    # 'w'	เขียนไฟล์ (write) ล้างข้อมูลเก่า
    # 'a'	เขียนต่อท้ายไฟล์ (append)
    # 'rb'	อ่านไฟล์ในรูปแบบไบนารี
    # 'wb'	เขียนไฟล์แบบไบนารี

    print("===7===") #################################################
    # โหมดการเปิดไฟล์ในภาษา Python (File Modes)
    # การเปิดไฟล์ต้องระบุ โหมด (mode) เพื่อกำหนดว่าเราจะ อ่าน (Input File) หรือ เขียน (Output File) ไฟล์นั้นอย่างไร
    #________________________________________
    #  โหมดหลักในการเปิดไฟล์
    # 'r'	เปิดไฟล์เพื่อ อ่านข้อมูล (default) ไฟล์ต้องมีอยู่หากไม่พบจะเกิดข้อผิดพลาด
    # 'w'	สร้างไฟล์ใหม่เพื่อ เขียนข้อมูลหากไฟล์มีอยู่แล้วข้อมูลเดิมจะถูกลบทิ้ง
    # 'x'	สร้างไฟล์ใหม่เพื่อเขียนข้อมูลหากไฟล์มีอยู่แล้วจะเกิดข้อผิดพลาด
    # 'a'	เปิดไฟล์เพื่อ เพิ่มข้อมูลต่อท้ายหากไม่มีไฟล์จะสร้างใหม่อัตโนมัติ
    #________________________________________
    #  โหมดเสริม (ใช้ร่วมกับโหมดหลัก)
    # 't'	เปิดไฟล์ในโหมด ข้อความ (text) เป็นค่าเริ่มต้นไม่ระบุก็ได้
    # 'b'	เปิดไฟล์ในโหมด ไบนารี (binary) เช่น เปิดรูปภาพ ไฟล์เสียง
    # '+'	เปิดไฟล์เพื่อ อ่านและเขียนข้อมูลได้ทั้งคู่ใช้ร่วมกับ'r', 'w', 'a' หรือ'x'ได้

    # fo = open("mydata.txt")          # ใช้ค่า default โหมดอ่านเท็กซ์ไฟล์
    fo = open("mydata.txt",mode="w") # โหมดเขียนเท็กซ์ไฟล์          # 'w'	สร้างไฟล์ใหม่เพื่อ เขียนข้อมูลหากไฟล์มีอยู่แล้วข้อมูลเดิมจะถูกลบทิ้ง
    fo = open("mydata.txt","rt")     # โหมดอ่านเท็กไฟล์            # 'r'	เปิดไฟล์เพื่อ อ่านข้อมูล (default)  # 't'	เปิดไฟล์ในโหมด ข้อความ (text)
    fo = open("mydata.txt","wb")     # โหมดเขียนไบนารีไฟล์         # 'w'	เขียนไฟล์ (write) ล้างข้อมูลเก่า # 'b'	เปิดไฟล์ในโหมด ไบนารี (binary) เช่น เปิดรูปภาพ ไฟล์เสียง
    fo = open("mydata.txt","wb+")    # โหมดเขียนและอ่านไบนารีไฟล์    # 'w'	เขียนไฟล์ (write) ล้างข้อมูลเก่า # 'b'	เปิดไฟล์ในโหมด ไบนารี # '+'	เปิดไฟล์เพื่อ อ่านและเขียนข้อมูล

    print("===9===")  ###################################################
    # การเข้ารหัสตัวอักษร (Encoding)
    # การเข้ารหัสตัวอักษรคือการกำหนดรูปแบบการแปลง ข้อความ (text) ให้เป็น รหัสตัวเลข
    # เพื่อให้สามารถจัดเก็บลงไฟล์ หรือส่งผ่านข้อมูลได้อย่างถูกต้อง และสามารถแปลงกลับมาใช้งานได้เมื่อเปิดไฟล์
    # เมื่อทำงานกับไฟล์ข้อความในภาษา Python เราสามารถกำหนดรูปแบบการเข้ารหัสได้ด้วยพารามิเตอร์ encoding

    # การเข้ารหัส 0 ถึง 255 ขนาด 8 บิต หรือ 1 ไบต์ คือ Ascii
    # การเข้ารหัสเป็น ยูนิโค้ดแบบ 8 บิต (utf-8)
    # การเข้ารหัสเป็นยูนิโค้ดแบบ 16 บิต (UTF_16)

    # ASCII	8 บิต (1 ไบต์)	เข้ารหัสตัวอักษรพื้นฐาน เช่น A–Z, 0–9, สัญลักษณ์ทั่วไป รองรับสูงสุด 256 ตัวอักษร
    # UTF-8	8 บิตเป็นพื้นฐาน	เป็นรูปแบบ Unicode ที่นิยมมาก รองรับตัวอักษรทุกภาษา ขนาดเปลี่ยนตามข้อมูล (1–4 ไบต์)
    # UTF-16	16 บิต	เข้ารหัสแบบ Unicode เช่นกัน รองรับตัวอักษรได้หลากหลายกว่า ASCII ใช้ 2 ไบต์หรือมากกว่า

    fo = open("mydata.txt","w",encoding="latin1")
    fo = open("mydata.txt","r",encoding="utf-8")
    fo = open("mydata.txt","wt",encoding="UTF_8")

    print("===10===")  ###################################################
    #การปิดไฟล์เป็นการยกเลิกการเชื่มต่อกับไฟล์ และคืนค่าหน่วยความจำที่ใช้คืนให้ระบบ โดยใช้คำสั่ง close โดยมีรูปแบบดังนี้
    #fo.close()
    fo = open("mydata.txt","w")
    fo.close()

    print("===11===")  ###################################################
    fo = open("mydata.txt", mode="w")
    print("Open text file: mydata.txt")
    fo.close()
    print("Now closed file.")

    print("===12===") ###################################################
    #คำสั่ง write เป็นเมธอดในไฟล์ออบเจ็กต์ รับค่าอาร์กิวเม็นต์เป็นข้อความมาเขียนเก็บลงในไฟล์
    # และมีการคืนค่ากลับมาเป็นจำนวนตัวอักษรที่ได้เขียนเก็บลงไป

    fout = open("mydata.txt", "w") # open text file for write
    size = fout.write("Hello, Python File") # size = 18
    fout.close()

    # writelines() เป็น เมธอดของไฟล์ออบเจ็กต์ ที่ใช้สำหรับ เขียนข้อมูลหลายบรรทัดลงในไฟล์
    # โดยรับอาร์กิวเมนต์เป็น ข้อมูลคอลเลกชันแบบ list หรือ iterable ซึ่งเก็บข้อความไว้เป็นแต่ละบรรทัด

    print("===13===")  ###################################################

    datas1 = ["Somchai", "Cheingpongpan", "\n"]
    datas2 = ("Python", "File", "\n")
    fout = open("mydata.txt", "w")
    fout.writelines(datas1)
    fout.writelines(datas2)

    print("===14===")  ###################################################

    # # 1
    # datas1 = ["Somchai", "Cheingpongpan", "\n"]
    # datas2 = ["Python","File","\n"]
    # datas3 = {"name":"Somchai","surname":"Cheingpongpan"}
    # fout = open("mydata.txt","w") # 'w'	เขียนไฟล์ (write) ล้างข้อมูลเก่า
    # print(fout.write("Hello, text file\n")) #คำสั่ง write เป็นเมธอดในไฟล์ออบเจ็กต์ รับค่าอาร์กิวเม็นต์เป็นข้อความมาเขียนเก็บลงในไฟล์
    # fout.write("Salary : " + str(1200.5) + "\n")
    # fout.writelines(datas1) # writelines() เป็น เมธอดของไฟล์ออบเจ็กต์ ที่ใช้สำหรับ เขียนข้อมูลหลายบรรทัดลงในไฟล์
    # fout.writelines(datas2)
    # fout.writelines(datas3)
    # fout.close()

    datas1 = ["somchai", "cheingpongpan","\n"]
    datas2 = ("Python", "File", "\n")
    datas3 = {"name":"Somchai","surname":"cheingpongpan"}
    fout = open("mydata.txt","w")
    fout.write("Hello, text file\n") # เขียนได้บรรทีัดเดียว
    fout.write("Salary : 1200.5\n" )
    fout.writelines(datas1) # เขียนได้หลายบรรทัด หรือ list tuple dictionary
    fout.writelines(datas2)
    fout.writelines(datas3)
    fout.close()

    print("\n===16===")  ###################################################
    #1
    from random import randint

    fout = open("myscore.txt",mode="w")
    print("Open file myscore.txt")
    scores = []
    for n in range(10):
        scores.append(str(randint(1,100))+ "\n")
    print("Now, write score to file.")
    scoresStr = []
    fout.writelines(scores)
    fout.close()
    print("Now closed file.")

    # from random import randint
    # score = []f
    # fout = open("myscore.txt","w")
    # for i in range(10):
    #     score.append(str(randint(1, 100)) + "\n") # ทำให้ randint เป็น str เพื่อนใส่ \n
    # fout.writelines(score) # writelines เพื่อรับค่า list
    # fout.close()

    print("\n===18===")  ###################################################
    # read() เป็นเมธอดในไฟล์ออบเจ็กต์ ใช้สำหรับอ่านข้อมูลจากไฟล์
    # รูปแบบ: file.read([size])
    #  รับอาร์กิวเมนต์ size ซึ่งเป็นจำนวน ตัวอักษร ที่ต้องการอ่าน
    #  ถ้าไม่ระบุ size จะอ่านข้อมูล ทั้งหมด จากไฟล์
    # คืนค่าที่อ่านได้ในรูปของ สตริง (string)

    fin = open("mydata.txt","r")
    content1 = fin.read(10)  # อ่านขึ้นมา 10 ตัวอักษร
    content = fin.read()     # อ่านขึ้นมาจนหมดไฟล์
    fin.close()
    print(content1)
    print()
    print(content)

    print("\n===19===")  ###################################################
    # def main():
    #     print("Test open file for read.")
    #     fin = open("mydata.txt",encoding="utf-8")
    #     print("Open file mydata.txt")
    #     print("Use read to read data from flie.")
    #     data = fin.read()
    #     print(data)
    #     fin.close()
    #     print("Now closed file.")
    #
    # if __name__ == "__main__": #ถ้าไฟล์ Python นี้ ถูกรันโดยตรง (ไม่ใช่ถูกนำเข้าเป็นโมดูล) ให้เรียกฟังก์ชัน main()
    #     main()

    def main():
        print("Test open file for read.\nOpen file my data.txt\nUse read to read data from file")
        fin = open("mydata.txt",encoding="utf-8")
        data = fin.read()
        print(data)
        print("Now closed file.")

    if __name__ == "__main__":
        main()

    print("\n===21===")  ###################################################

    #  คำสั่ง readline()
    #  readline() เป็นเมธอดในไฟล์ออบเจ็กต์ ใช้สำหรับอ่าน หนึ่งบรรทัด จากไฟล์
    #  รูปแบบ file.readline([size])อ่านข้อมูลจากไฟล์ทีละบรรทัดจนกว่าจะเจออักขระขึ้นบรรทัดใหม่(\n)
    #  สามารถกำหนด size เพื่อระบุจำนวนตัวอักษรสูงสุดที่ต้องการอ่านได้
    #  หากไม่กำหนด size จะอ่านทั้งบรรทัด (รวม \n ด้วยถ้ามี)

    fin = open("mydata.txt","r")
    content1 = fin.readline(5) # อ่านขึ้นมา 5 ตัวอักษร
    content2 = fin.readline() # อ่านขึ้นมาจนเจอ \n
    print(content1)
    print(content2)
    fin.close()

    print("\n===22===")  ###################################################

    def read_data(filename):  # ฟังก์ชันสำหรับอ่านไฟล์ทีละบรรทัด แล้วคืนค่าเป็นลิสต์
        datas = []  # สร้างลิสต์เปล่าสำหรับเก็บข้อมูล
        fin = open(filename, encoding="utf-8")  # เปิดไฟล์ด้วย encoding แบบ utf-8
        data = fin.readline()  # อ่านบรรทัดแรกจากไฟล์
        while data != "":  # วนลูปจนกว่าจะถึงท้ายไฟล์
            datas.append(data)  # เพิ่มบรรทัดที่อ่านได้เข้าไปในลิสต์
            data = fin.readline()  # อ่านบรรทัดถัดไป
        return datas  # คืนค่าลิสต์ข้อมูลที่อ่านได้จากไฟล์

    def main():  # ฟังก์ชันหลักของโปรแกรม
        print("Open file my data.txt\nUse readline to read data from file.")  # แสดงข้อความบนหน้าจอ
        fin = open("mydata.txt", encoding="utf-8")  # เปิดไฟล์ mydata.txt
        data1 = fin.readline(5)  # อ่าน 5 ตัวอักษรแรกของบรรทัดแรก
        data2 = fin.readline()  # อ่านข้อมูลต่อจากตำแหน่งเดิมจนถึงจบบรรทัด
        print(data1 + "+" + data2)  # แสดงผลรวมข้อความของ data1 กับ data2 คั่นด้วย +
        print("Now closed file.")  # แสดงข้อความว่าไฟล์ถูกอ่านเสร็จแล้ว
        score = read_data("myscore.txt")  # เรียกใช้ฟังก์ชัน read_data เพื่ออ่านไฟล์ myscore.txt
        print(score)  # แสดงข้อมูลที่อ่านได้จากไฟล์ myscore.txt

    if __name__ == "__main__":  # ตรวจว่าไฟล์นี้ถูกรันโดยตรง ไม่ได้ถูก import จากไฟล์อื่น
        main()  # เรียกฟังก์ชัน main() เพื่อเริ่มทำงานของโปรแกรม

    # ทำซ็ำ
    # print("Open file mydata.txt\nUse readline to read data from file.")
    # fin = open("mydata.txt","r",encoding="utf-8")
    # data1 = fin.readline(5)
    # data2 = fin.readline()
    # print(data1 + "+" + data2)
    #
    # print("\nNow closed file.")
    # datas = [] # สร้างลิสต์เปล่าเพื่อเก็บข้อมูลที่อ่านได้
    # fin = open("myscore.txt",encoding="utf-8") # เปิดไฟล์แบบอ่าน (read mode)
    # data = fin.readline() # อ่านบรรทัดแรก
    # while data != "":  # วนลูปจนกว่าจะถึงท้ายไฟล์ (readline จะคืน "" เมื่อถึงท้ายไฟล์)
    #     datas.append(data) # เก็บบรรทัดที่อ่านได้ไว้ในลิสต์
    #     data = fin.readline() # อ่านบรรทัดถัดไป
    # fin.close() # ปิดไฟล์หลังอ่านเสร็จ
    # print(datas) # แสดงข้อมูลทั้งหมดในลิสต์

    #ทำซ้ำ 2
    # # แสดงข้อความบอกว่าเริ่มเปิดไฟล์ mydata.txt และจะใช้ readline อ่านข้อมูล
    # print("Open file mydata.txt\nUse readline to read data from file.")
    # # เปิดไฟล์ mydata.txt เพื่ออ่านข้อมูล โดยกำหนดให้ใช้รหัส utf-8
    # fin = open("mydata.txt", encoding="utf-8")
    # # อ่านข้อมูลจากไฟล์สูงสุด 5 ตัวอักษรแรกของบรรทัดแรก แล้วเก็บไว้ในตัวแปร data1
    # data1 = fin.readline(5)
    # # อ่านข้อมูลต่อจากบรรทัดเดิม หรือบรรทัดถัดไป แล้วเก็บไว้ในตัวแปร data2
    # data2 = fin.readline()
    # # แสดงข้อมูลที่อ่านได้จาก data1 และ data2 เชื่อมด้วยเครื่องหมาย +
    # print(data1 + "+" + data2)
    #
    # # แสดงข้อความว่าได้อ่านไฟล์เสร็จแล้ว
    # print("Now closed file.")
    # # สร้างลิสต์เปล่าเพื่อเก็บข้อมูลจากไฟล์ myscore.txt ทีละบรรทัด
    # datas = []
    # # เปิดไฟล์ myscore.txt เพื่ออ่านข้อมูล โดยกำหนดให้ใช้รหัส utf-8
    # fin = open("myscore.txt", encoding="utf-8")
    # # อ่านบรรทัดแรกจากไฟล์
    # data = fin.readline()
    # # วนลูปอ่านไฟล์ทีละบรรทัดจนกว่าจะเจอข้อมูลว่าง (จบบรรทัดสุดท้ายของไฟล์)
    # while data != "":
    #     datas.append(data)  # เพิ่มบรรทัดที่อ่านได้เข้าไปในลิสต์ datas
    #     data = fin.readline()  # อ่านบรรทัดถัดไป
    # # ปิดไฟล์เมื่ออ่านข้อมูลเสร็จ
    # fin.close()
    # # แสดงลิสต์ datas ที่เก็บข้อมูลจากไฟล์ myscore.txt
    # print(datas)

    print("\n===25===") #############################################################
    # readlines() เป็นเมธอดในไฟล์ออบเจ็กต์ ใช้สำหรับอ่านข้อมูล ทั้งหมดจากไฟล์ แล้ว แบ่งออกเป็นแต่ละบรรทัด
    # รูปแบบ: file.readlines()
    # อ่านข้อมูลทั้งไฟล์ในครั้งเดียว
    # คืนค่าข้อมูลในรูปแบบ ลิสต์ (list) ซึ่งแต่ละสมาชิกในลิสต์คือ หนึ่งบรรทัด จากไฟล์
    # แต่ละบรรทัดจะยังคงมีตัวขึ้นบรรทัดใหม่ \n ติดมาด้วย (ถ้ามีในไฟล์)

    fin = open("mydata.txt","r")
    content = fin.readlines() # อ่านขึ้นมาทั้งหมดเป็นแบบ list ใช้สำหรับอ่านข้อมูล ทั้งหมดจากไฟล์ แล้ว แบ่งออกเป็นแต่ละบรรทัด
    print(content)
    fin.close()

    print("\n===26===")   ########################################################################################
    # def read_data(filename):  # ฟังก์ชันสำหรับอ่านข้อมูลจากไฟล์แบบแยกบรรทัด (คืนค่าเป็นลิสต์)
    #     fin = open(filename, encoding="utf-8")  # เปิดไฟล์ด้วย encoding เป็น utf-8
    #     datas = fin.readlines()  # อ่านข้อมูลทั้งหมดจากไฟล์และแยกเป็นลิสต์ตามบรรทัด
    #     fin.close()  # ปิดไฟล์หลังอ่านข้อมูลเสร็จ
    #     return (datas)  # คืนค่าลิสต์ข้อมูลที่อ่านได้
    #
    # def main():  # ฟังก์ชันหลักของโปรแกรม
    #     scores = read_data("myscore.txt")  # เรียกใช้ read_data เพื่ออ่านข้อมูลจากไฟล์ myscore.txt
    #     print(scores)  # แสดงผลข้อมูลจากไฟล์ myscore.txt
    #     datas = read_data("mydata.txt")  # เรียกใช้ read_data เพื่ออ่านข้อมูลจากไฟล์ mydata.txt
    #     print(datas)  # แสดงผลข้อมูลจากไฟล์ mydata.txt
    #
    # if __name__ == "__main__":  # ตรวจสอบว่าโปรแกรมนี้ถูกรันโดยตรง (ไม่ใช่ถูก import)
    #     main()  # เรียกใช้ฟังก์ชัน main() เพื่อเริ่มต้นโปรแกรม

    def read_data(filename):
        fin = open(filename,encoding="utf-8") # เปิด def ไว้สำหรับอยากอ่านหลายไฟล์โดย แค่ให้ main ใส่ชื่อ filename
        datas = fin.readlines()
        fin.close()
        return datas

    def main():
        scores = read_data("myscore.txt")
        print(scores)
        datas = read_data("mydata.txt")
        print(datas)

    if __name__ == "__main__":
        main()

    # ทำซ้ำ
    # fin = open("myscore.txt",encoding="utf-8")
    # data = fin.readlines()
    # print(data)
    # fin = open("mydata.txt",encoding="utf-8")
    # data = fin.readlines()
    # print(data)

    print("\n===28===")   ########################################################################################

    # with เป็น Context Manager ในภาษา Python
    # ใช้สำหรับจัดการทรัพยากร เช่น ไฟล์ ให้อย่างปลอดภัยและอัตโนมัติ
    # สามารถ เปิดไฟล์หลายไฟล์พร้อมกัน
    # ไม่ต้องเขียน close() เอง เพราะ Python จะปิดไฟล์ให้อัตโนมัติเมื่อออกจากบล็อก with

    #with open(filename, mode, encoding) as file_object1,
    #     open(filename, mode, encoding) as file_object2,
    #     open(filename, mode, encoding) as file_object3:
    #   statements

    #ตัวอย่าง
    # with open("filename.txt", encoding="utf-8") as f:
    #     # ใช้งานไฟล์ f ได้ภายในบล็อกนี้
    #     data = f.read()
    # # ออกจากบล็อกแล้ว ไฟล์จะถูกปิดให้อัตโนมัติ

    # ตัวอย่าง
    # with open("file1.txt") as f1, open("file2.txt") as f2:
    #     data1 = f1.read()
    #     data2 = f2.read()

    # with open("mydata.txt") as fin, open("myoutput.txt","w") as fout:
    #     data = fin.readline()
    #     while data != "":
    #         print(data)
    #         fout.write(data)
    #         data = fin.readline()
    #
    with open("mydata.txt") as fin, open("myoutput.txt","w") as fout:  # เปิดไฟล์ mydata.txt สำหรับอ่าน และ myoutput.txt สำหรับเขียน (ทั้งสองไฟล์จะปิดอัตโนมัติเมื่อจบบล็อก)
        data = fin.readline()  # อ่านบรรทัดแรกจากไฟล์ mydata.txt
        while data != "":  # วนลูปจนกว่าจะอ่านถึงท้ายไฟล์ (เมื่อได้ค่าเป็นสตริงว่าง "")
            print(data)  # แสดงบรรทัดที่อ่านได้ทางหน้าจอ
            fout.write(data)  # เขียนบรรทัดที่อ่านได้ลงไฟล์ myoutput.txt
            data = fin.readline()  # อ่านบรรทัดถัดไปจากไฟล์ mydata.txt

    print("\n===29===\n")   ########################################################################################
    # def read_data():  # ฟังก์ชันสำหรับอ่านข้อมูลจากไฟล์ mydata.txt แบบทีละบรรทัด
    #     with open("mydata.txt", encoding="utf-8") as fin:  # เปิดไฟล์ mydata.txt โดยใช้ encoding เป็น utf-8
    #         data = fin.readline()  # อ่านบรรทัดแรกจากไฟล์
    #         while data != "":  # วนลูปจนกว่าจะถึงท้ายไฟล์ (data เป็นสตริงว่าง)
    #             print(data)  # แสดงบรรทัดที่อ่านได้
    #             data = fin.readline()  # อ่านบรรทัดถัดไป
    #     print("finish read.\n")  # แสดงข้อความเมื่ออ่านไฟล์เสร็จ
    #
    # def read_and_write():  # ฟังก์ชันสำหรับอ่านจากไฟล์แล้วเขียนไปยังอีกไฟล์
    #     with (  # ใช้ with แบบเปิดไฟล์ 2 ไฟล์พร้อมกัน
    #         open("mydata.txt", encoding="utf-8") as fin,  # เปิดไฟล์ต้นทางเพื่ออ่าน
    #         open("myoutput.txt", "w", encoding="utf-8") as fout  # เปิดไฟล์ปลายทางเพื่อเขียน (โหมดเขียนทับ)
    #     ):
    #         for line in fin:  # วนลูปอ่านแต่ละบรรทัดจากไฟล์ต้นทาง
    #             print(line)  # แสดงบรรทัดที่อ่านได้
    #             fout.writelines(line)  # เขียนบรรทัดนั้นลงไฟล์ปลายทาง (จริง ๆ ใช้ write() จะเหมาะกว่า)
    #     print("finish read and write file.\n")  # แสดงข้อความเมื่อเสร็จสิ้นการอ่านและเขียนไฟล์
    #
    # def main():  # ฟังก์ชันหลักสำหรับแสดงเมนูและรับคำสั่งจากผู้ใช้
    #     menu = "Main Menu\n===========\n1. Read Data\n2. Read and Write\n"  # เมนูแสดงตัวเลือก
    #     menu += "3. Exit\nEnter Choice :"  # ต่อข้อความเมนูให้สมบูรณ์
    #     while True:  # วนลูปรับค่าจากผู้ใช้ไปเรื่อย ๆ
    #         choice = input(menu)  # รับค่าจากผู้ใช้
    #         if choice == "1":  # ถ้าเลือก 1
    #             read_data()  # เรียกฟังก์ชันอ่านไฟล์
    #         elif choice == "2":  # ถ้าเลือก 2
    #             read_and_write()  # เรียกฟังก์ชันอ่านและเขียนไฟล์
    #         elif choice == "3":  # ถ้าเลือก 3
    #             print("Exit program.")  # แสดงข้อความออกจากโปรแกรม
    #             break  # หยุดลูปเพื่อออกจากโปรแกรม
    #
    # if __name__ == "__main__":  # ตรวจสอบว่าไฟล์นี้ถูกรันโดยตรง (ไม่ใช่ถูก import)
    #     main()  # เรียกใช้งานฟังก์ชัน main()

    # def read_data():
    #     with open("mydata.txt",encoding="utf-8") as fin:
    #         data = fin.readline()
    #         while data != "":
    #             print(data)
    #             data = fin.readline()
    #     print("finish read.")
    #
    # def read_and_write():
    #     with (open("mydata.txt",encoding="utf-8") as fin,
    #         open("myoutput.txt","w",encoding="utf-8") as fout
    #           ):
    #         for i in fin:
    #             print(i)
    #             fout.writelines(i)
    #         print("finish read and write file.")
    #
    # def main():
    #     while True:
    #         menu = "Main Menu\n===========\n1. Read Data\n2. Read and Write\n3. Exit\nEnter Choice : "
    #         choice = int(input(menu))
    #         if choice == 1:
    #             read_data()
    #         elif choice == 2:
    #             read_and_write()
    #         elif choice == 3:
    #             print("Exit program.")
    #             break
    #         else:
    #             print("No choice")
    #
    # if __name__ == "__main__":
    #     main()

    print("\n===32===\n")   ########################################################################################
    from w7.ModuleEmployee import add_employee,report_employee,read_file,read_to_memory

    DATAFILE = "employee.txt"

    def main():
        menu = ("=" * 17) + "\n| Employee Menu |\n" + ("=" * 17)
        menu += ("\n1. Add Employee\n2. Display Employee from File\n")
        menu += "3. Read Employee Data to Memory\n4. Report Employee\n"
        menu += "5. Exit\nEnter Choice : "
        while True:
            choice = input(menu)
            if choice == "1":
                add_employee(DATAFILE)
            elif choice == "2":
                read_file(DATAFILE)
            elif choice == "3":
                datas = read_to_memory(DATAFILE)
            elif choice == "4":
                report_employee(datas)
            elif choice == "5":
                print("Exit Program")
                break
            else:
                print("No choice, input again.")

    if __name__ == "__main__":
        main()
s()