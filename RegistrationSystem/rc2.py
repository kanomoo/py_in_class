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
    courses = load_data("main_rc/courses.json")
    while True:
        print("\nCourse Management")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            course_id = input("Enter Course ID: ")
            course_name = input("Enter Course Name: ")
            credit = int(input("Enter Credit Hours: "))
            courses.append({"id": course_id, "name": course_name, "credit": credit})
            save_data("main_rc/courses.json", courses)
            print("Course added successfully!")
        elif choice == "2":
            print("\nCourses:")
            for course in courses:
                print(f"ID: {course['id']}, Name: {course['name']}, Credit: {course['credit']}")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_students():
    students = load_data("main_rc/students.json")
    while True:
        print("\nStudent Management")
        print("1. Add Student")
        print("2. View Students")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            student_id = input("Enter Student ID: ")
            student_name = input("Enter Student Name: ")
            students.append({"id": student_id, "name": student_name})
            save_data("main_rc/students.json", students)
            print("Student added successfully!")
        elif choice == "2":
            print("\nStudents:")
            for student in students:
                print(f"ID: {student['id']}, Name: {student['name']}")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def register_courses():
    registrations = load_data("main_rc/registrations.json")
    students = load_data("main_rc/students.json")
    courses = load_data("main_rc/courses.json")
    while True:
        print("\nCourse Registration")
        print("1. Register a Student for a Course")
        print("2. View Registrations")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            student_id = input("Enter Student ID: ")
            course_id = input("Enter Course ID: ")
            if any(student['id'] == student_id for student in students) and \
               any(course['id'] == course_id for course in courses):
                registrations.append({"student_id": student_id, "course_id": course_id, "grade": None})
                save_data("main_rc/registrations.json", registrations)
                print("Registration successful!")
            else:
                print("Invalid Student ID or Course ID.")
        elif choice == "2":
            print("\nRegistrations:")
            for reg in registrations:
                print(f"Student ID: {reg['student_id']}, Course ID: {reg['course_id']}, Grade: {reg['grade']}")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def record_grades():
    registrations = load_data("main_rc/registrations.json")
    while True:
        print("\nGrade Recording")
        print("1. Record Grade for a Student")
        print("2. View Grades")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            student_id = input("Enter Student ID: ")
            course_id = input("Enter Course ID: ")
            grade = input("Enter Grade: ")
            for reg in registrations:
                if reg['student_id'] == student_id and reg['course_id'] == course_id:
                    reg['grade'] = grade
                    save_data("main_rc/registrations.json", registrations)
                    print("Grade recorded successfully!")
                    break
            else:
                print("Registration not found.")
        elif choice == "2":
            print("\nGrades:")
            for reg in registrations:
                print(f"Student ID: {reg['student_id']}, Course ID: {reg['course_id']}, Grade: {reg['grade']}")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def generate_gpa_report():
    registrations = load_data("main_rc/registrations.json")
    students = load_data("main_rc/students.json")
    courses = load_data("main_rc/courses.json")
    print("\nGPA Report")
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
        print(f"Student ID: {student_id}, Name: {student['name']}, GPA: {gpa:.2f}")

def main_menu():
    while True:
        print("\nRegistration System")
        print("1. Manage Courses")
        print("2. Manage Students")
        print("3. Register Courses")
        print("4. Record Grades")
        print("5. Generate GPA Report")
        print("6. Exit")
        choice = input("Enter your choice: ")
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
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()