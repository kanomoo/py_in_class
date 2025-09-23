
def enter_employee(filename):
    print("Enter data employee.")
    emp_id = input("Input employee id : ")
    emp_name = input("Input employee name : ")
    emp_surname = input("Input employee surname : ")
    emp_salary = input("Input employee salary : ")
    fout = open(filename,"a",encoding="UTF-8")
    fout.write(emp_id + "," + emp_name + "," + emp_surname + "," + emp_salary + "\n")
    fout.close()

def read_employee(filename):
    with open(filename) as fin:
        for i in fin:
            print(i)

def read_employee_data(filename):
    data = []
    with open(filename) as fin:
        for i in fin:
            i = i.rstrip("\n")
            data.append(i.split(","))
    return data

def report(data):
    head = "| No.|  Id  |  Name    |  Surname    |  Salary  |"
    line = "-" * len(head)
    print(format("Report Employee","^49"))
    print(line,head,line,sep="\n")
    n = 1
    for i in data:
        print(f"| {n:2} | {i[0]:^5}|{i[1]:^10}|{i[2]:^13}|{float(i[3]):10.2f}|")
        n += 1
    print(line)

def main():
    filename = "employee.txt"
    head = "| Employee Menu |"
    line = "=" * len(head)
    while True:
        print(line,head,line,sep="\n")
        menu = "1. Add Employee\n2. Display Employee From File\n3. Read Employee Data to Memory\n4. Report Employee\n5. Exit\n"
        menu += "Enter choice : "
        choice = input(menu)
        print()
        if choice == "1":
            enter_employee(filename)
        elif choice == "2":
            read_employee(filename)
        elif choice == "3":
            data = read_employee_data(filename)
        elif choice == "4":
            report(data)
        elif choice == "5":
            print("Exit Program")
            break
        else:
            print("No choice, input again.")

if __name__ == "__main__":
    main()