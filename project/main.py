import sys
from product import ProductManager
from employee import EmployeeManager
from sale import SaleManager
from report import ReportManager

def main_menu():
    print("\n=== Coffee Shop System ===")
    print("1. Manage Products")
    print("2. Manage Employees")
    print("3. Record Sale")
    print("4. Reports")
    print("0. Exit")
    return input("Select menu: ")

def report_menu():
    print("\n--- Reports ---")
    print("1. Product List")
    print("2. Employee List")
    print("3. Daily Sales Summary")
    print("4. Sales by Employee")
    print("5. Sales by Product")
    print("6. Employee Commission")
    print("0. Back")
    return input("Select report: ")

product_mgr = ProductManager()
employee_mgr = EmployeeManager()
sale_mgr = SaleManager()
report_mgr = ReportManager(product_mgr, employee_mgr, sale_mgr)

while True:
    choice = main_menu()
    if choice == "1":
        product_mgr.menu()
    elif choice == "2":
        employee_mgr.menu()
    elif choice == "3":
        sale_mgr.menu(product_mgr, employee_mgr)
    elif choice == "4":
        while True:
            r_choice = report_menu()
            if r_choice == "1":
                report_mgr.show_products()
            elif r_choice == "2":
                report_mgr.show_employees()
            elif r_choice == "3":
                report_mgr.daily_sales()
            elif r_choice == "4":
                report_mgr.sales_by_employee()
            elif r_choice == "5":
                report_mgr.sales_by_product()
            elif r_choice == "6":
                report_mgr.employee_commission()
            elif r_choice == "0":
                break
    elif choice == "0":
        sys.exit()
    else:
        print("Invalid choice.")
