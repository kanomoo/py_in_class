# ฟังก์ชัน calculate_grade ใช้สำหรับคำนวณเกรดและคะแนน (Point) จากคะแนนที่ได้รับ (score)
# ฟังก์ชันนี้ใช้ return เพื่อส่งค่ากลับไปยังส่วนที่เรียกใช้งาน
# return มีประโยชน์เพราะช่วยให้เราส่งค่าผลลัพธ์ออกจากฟังก์ชันไปใช้งานต่อได้
def calculate_grade(score):
    # ตรวจสอบช่วงคะแนนและกำหนดเกรดกับคะแนน (Point) ตามเงื่อนไข
    if score >= 80:
        return 'A', 4.0  # ส่งค่าเกรด 'A' และคะแนน 4.0 กลับไป
    elif score >= 70:
        return 'B', 3.0
    elif score >= 60:
        return 'C', 2.0
    elif score >= 50:
        return 'D', 1.0
    else:
        return 'F', 0.0  # กรณีคะแนนน้อยกว่า 50 จะได้เกรด 'F' และคะแนน 0.0

# ฟังก์ชัน main เป็นส่วนหลักของโปรแกรมที่ทำหน้าที่รวบรวมข้อมูล คำนวณ และแสดงผล
def main():
    subject = []  # สร้างลิสต์เปล่าสำหรับเก็บข้อมูลของแต่ละวิชา
    total_points = 0  # ตัวแปรสำหรับเก็บคะแนนรวม
    total_credits = 0  # ตัวแปรสำหรับเก็บหน่วยกิตรวม

    # แสดงข้อความต้อนรับผู้ใช้งาน
    print("ProgramCalculateGrade")
    print("\nInput Data:")

    # ใช้ลูป for เพื่อรับข้อมูลคะแนนและหน่วยกิตของแต่ละวิชา
    for i in range(1, 7):  # ลูปตั้งแต่ 1 ถึง 6 (รวม 6 วิชา)
        # รับคะแนนของวิชา โดยใช้ input() และแปลงเป็น float
        score = float(input(f"Enter score of subject  #{i} : "))
        # รับหน่วยกิตของวิชา โดยใช้ input() และแปลงเป็น int
        credit = int(input(f"Enter credit of subject #{i} : "))
        # เรียกใช้ฟังก์ชัน calculate_grade เพื่อคำนวณเกรดและคะแนน
        grade, point = calculate_grade(score)
        # เก็บข้อมูลของวิชาในรูปแบบ tuple และเพิ่มลงในลิสต์ subject
        # tuple คือโครงสร้างข้อมูลที่เก็บค่าหลายค่าไว้ด้วยกันในรูปแบบที่ไม่สามารถเปลี่ยนแปลงได้ (immutable)
        # ใช้ () ในการสร้าง tuple เช่น (1, 90.5, 'A', 3, 12.0)
        # ในที่นี้ tuple ถูกใช้เพื่อเก็บข้อมูลของวิชา เช่น ลำดับวิชา, คะแนน, เกรด, หน่วยกิต และคะแนนรวม
        subject.append((i, score, grade, credit, point * credit))
        # คำนวณคะแนนรวม (Point * Credit) และเพิ่มใน total_points
        total_points += point * credit
        # เพิ่มหน่วยกิตใน total_credits
        total_credits += credit

    # แสดงรายงานผลการคำนวณ
    print("\n         Report Grade")
    print("==================================")
    print("|No.|  Mark |Grade|Credit| Points|")
    print("==================================")
    # ใช้ลูป for เพื่อแสดงข้อมูลของแต่ละวิชา
    for s in subject:
        # ใช้ f-string เพื่อจัดรูปแบบข้อความให้อ่านง่าย
        # f-string (formatted string) เป็นวิธีการจัดรูปแบบข้อความใน Python
        # โดยการใส่ตัวอักษร 'f' ไว้หน้าสตริง และใช้ {} เพื่อใส่ตัวแปรหรือโค้ดที่ต้องการแสดงผล
        # เช่น f"คะแนนของคุณคือ {score}" จะนำค่าของตัวแปร score มาแสดงในข้อความ
        print(f"| {s[0]} |  {s[1]} |  {s[2]}  |   {s[3]}  |  {s[4]:4.1f} |")
    print("==================================")
    # แสดงผลรวมของหน่วยกิตและคะแนนรวม
    print(f"|      Total      | {total_credits:.1f} |  {total_points} |")
    print("==================================")
    # คำนวณและแสดงค่าเฉลี่ยคะแนน (GPA)
    print(f"Grade Point Average(GPA) : {total_points / total_credits:.2f}")

# เรียกใช้ฟังก์ชัน main เพื่อเริ่มต้นโปรแกรม
main()