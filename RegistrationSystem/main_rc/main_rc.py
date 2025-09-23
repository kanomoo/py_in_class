import json

def load_data(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def manage_courses():
    courses = load_data("courses.json")
    while True:
        print("\nจัดการรายวิชา")
        print("1. เพิ่มรายวิชา")
        print("2. ดูรายวิชา")
        print("3. กลับไปเมนูหลัก")
        choice = input("กรุณาเลือกตัวเลือก: ")
        if choice == "1":
            course_id = input("กรุณาใส่รหัสรายวิชา: ")
            course_name = input("กรุณาใส่ชื่อรายวิชา: ")
            credit = int(input("กรุณาใส่จำนวนหน่วยกิต: "))
            courses.append({"id": course_id, "name": course_name, "credit": credit})
            save_data("courses.json", courses)
            print("เพิ่มรายวิชาเรียบร้อยแล้ว!")
        elif choice == "2":
            print("\nรายวิชา:")
            for course in courses:
                print(f"รหัส: {course['id']}, ชื่อ: {course['name']}, หน่วยกิต: {course['credit']}")
        elif choice == "3":
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง.")

def manage_students():
    students = load_data("students.json")
    while True:
        print("\nจัดการนักศึกษา")
        print("1. เพิ่มนักศึกษา")
        print("2. ดูนักศึกษา")
        print("3. กลับไปเมนูหลัก")
        choice = input("กรุณาเลือกตัวเลือก: ")
        if choice == "1":
            student_id = input("กรุณาใส่รหัสนักศึกษา: ")
            student_name = input("กรุณาใส่ชื่อนักศึกษา: ")
            students.append({"id": student_id, "name": student_name})
            save_data("students.json", students)
            print("เพิ่มนักศึกษาเรียบร้อยแล้ว!")
        elif choice == "2":
            print("\nนักศึกษา:")
            for student in students:
                print(f"รหัส: {student['id']}, ชื่อ: {student['name']}")
        elif choice == "3":
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง.")

def register_courses():
    registrations = load_data("registrations.json")
    students = load_data("students.json")
    courses = load_data("courses.json")
    while True:
        print("\nลงทะเบียนรายวิชา")
        print("1. ลงทะเบียนนักศึกษาในรายวิชา")
        print("2. ดูการลงทะเบียน")
        print("3. กลับไปเมนูหลัก")
        choice = input("กรุณาเลือกตัวเลือก: ")
        if choice == "1":
            student_id = input("กรุณาใส่รหัสนักศึกษา: ")
            course_id = input("กรุณาใส่รหัสรายวิชา: ")
            if any(student['id'] == student_id for student in students) and \
               any(course['id'] == course_id for course in courses):
                registrations.append({"student_id": student_id, "course_id": course_id, "grade": None})
                save_data("registrations.json", registrations)
                print("ลงทะเบียนเรียบร้อยแล้ว!")
            else:
                print("รหัสนักศึกษาหรือรหัสรายวิชาไม่ถูกต้อง.")
        elif choice == "2":
            print("\nการลงทะเบียน:")
            for reg in registrations:
                print(f"รหัสนักศึกษา: {reg['student_id']}, รหัสรายวิชา: {reg['course_id']}, เกรด: {reg['grade']}")
        elif choice == "3":
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง.")

def record_grades():
    registrations = load_data("registrations.json")
    while True:
        print("\nบันทึกเกรด")
        print("1. บันทึกเกรดให้นักศึกษา")
        print("2. ดูเกรด")
        print("3. กลับไปเมนูหลัก")
        choice = input("กรุณาเลือกตัวเลือก: ")
        if choice == "1":
            student_id = input("กรุณาใส่รหัสนักศึกษา: ")
            course_id = input("กรุณาใส่รหัสรายวิชา: ")
            grade = input("กรุณาใส่เกรด: ")
            for reg in registrations:
                if reg['student_id'] == student_id and reg['course_id'] == course_id:
                    reg['grade'] = grade
                    save_data("registrations.json", registrations)
                    print("บันทึกเกรดเรียบร้อยแล้ว!")
                    break
            else:
                print("ไม่พบการลงทะเบียน.")
        elif choice == "2":
            print("\nเกรด:")
            for reg in registrations:
                print(f"รหัสนักศึกษา: {reg['student_id']}, รหัสรายวิชา: {reg['course_id']}, เกรด: {reg['grade']}")
        elif choice == "3":
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง.")

def generate_gpa_report():
    registrations = load_data("registrations.json")
    students = load_data("students.json")
    courses = load_data("courses.json")
    print("\nรายงาน GPA")
    for student in students:
        student_id = student['id']
        total_points = 0
        total_credits = 0
        for reg in registrations:
            if reg['student_id'] == student_id and reg['grade'] is not None:
                course = next((c for c in courses if c['id'] == reg['course_id']), None)
                if course:
                    grade_point = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}.get(reg['grade'], 0.0)
                    total_points += grade_point * course['credit']
                    total_credits += course['credit']
        gpa = total_points / total_credits if total_credits > 0 else 0.0
        print(f"รหัสนักศึกษา: {student_id}, ชื่อ: {student['name']}, GPA: {gpa:.2f}")

def main_menu():
    while True:
        print("\nระบบลงทะเบียน")
        print("1. จัดการรายวิชา")
        print("2. จัดการนักศึกษา")
        print("3. ลงทะเบียนรายวิชา")
        print("4. บันทึกเกรด")
        print("5. สร้างรายงาน GPA")
        print("6. ออกจากระบบ")
        choice = input("กรุณาเลือกตัวเลือก: ")
        if choice == "1":
            manage_courses()
        elif choice == "2":
            manage_students()
        elif choice == "3":
            register_courses()
        elif choice == "4":
            record_grades()
        elif choice == "5":
            generate_gpa_report()
        elif choice == "6":
            print("ออกจากระบบ ลาก่อน!")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง.")

if __name__ == "__main__":
    main_menu()