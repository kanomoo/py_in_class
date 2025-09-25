from ModuleEmployee import *
DATAFILE = r"AllChapter\chapter 9\employee.txt"
def main():
    menu = ("="*17)+"\n| Employee Menu |\n"+("="*17)
    menu += "\n1. Add Employee\n2. Display Employee from File\n"
    menu += "3. Report Employee\n"
    menu += "4. Exit\nEnter Choice : "
    while True:
        choice = input(menu)
        if choice == "1": add_emplyee(DATAFILE)
        elif choice == "2": read_file(DATAFILE)
        elif choice == "3": report_employee(DATAFILE)
        elif choice == "4": break
        else: print("No choice, input again.")
    print("Exit Program")

if __name__ == "__main__":
    main()