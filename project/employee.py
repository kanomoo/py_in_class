import csv

EMPLOYEE_FILE = "employees.csv"

class EmployeeManager:
    def __init__(self):
        self.employees = []
        self.load()

    def load(self):
        self.employees = []
        try:
            with open(EMPLOYEE_FILE, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.employees.append(row)
        except FileNotFoundError:
            pass

    def save(self):
        with open(EMPLOYEE_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["id", "name"])
            writer.writeheader()
            writer.writerows(self.employees)

    def menu(self):
        print("\n--- Employee Management ---")
        print("1. Add Employee")
        print("2. List Employees")
        print("0. Back")
        choice = input("Select: ")
        if choice == "1":
            self.add_employee()
        elif choice == "2":
            self.list_employees()
        elif choice == "0":
            return

    def add_employee(self):
        eid = input("Employee ID: ")
        name = input("Name: ")
        self.employees.append({"id": eid, "name": name})
        self.save()
        print("Employee added.")

    def list_employees(self):
        from tabulate import tabulate
        print(tabulate(self.employees, headers="keys", tablefmt="fancy_grid"))
