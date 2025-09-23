# personal finance tracker
income = []
expense = []

def add_income(amount: float, description: str) -> None:
    income.append(description)
    income.append(amount)

def add_expense(amount: float, description: str) -> None:
    expense.append(description)
    expense.append(amount)

def display_income_entries() -> None:
    print(income)

def display_expense_entries() -> None:
    print(expense)

def calculate_balance() -> float:
    return income[1] - expense[1]

add_income(1000.0,"Salary")
add_expense(150.0,"Groceries")
display_income_entries()
display_expense_entries()
print(calculate_balance())









# from typing import List
#
# # ตัวแปรเก็บข้อมูลรายรับและรายจ่าย
#
# income_entries: List[tuple] = []
# expense_entries: List[tuple] = []
#
# def add_income(amount: float, description: str) -> None:
#     if amount > 0 and description.strip() != "":
#         income_entries.append((amount, description))
#         print(f"Income added: {description} - {amount} Baht")
#     else:
#         print("Invalid income entry.")
#
# def add_expense(amount: float, description: str) -> None:
#     if amount > 0 and description.strip() != "":
#         expense_entries.append((amount, description))
#         print(f"Expense added: {description} - {amount} Baht")
#     else:
#         print("Invalid expense entry.")
#
# def display_income_entries() -> None:
#     if not income_entries:
#         print("No income entries.")
#     else:
#         print("Income Entries:")
#         for amount, desc in income_entries:
#             print(f"- {desc}: {amount} Baht")
#
# def display_expense_entries() -> None:
#     if not expense_entries:
#         print("No expense entries.")
#     else:
#         print("Expense Entries:")
#         for amount, desc in expense_entries:
#             print(f"- {desc}: {amount} Baht")
#
# def calculate_balance() -> float:
#     total_income = sum(amount for amount, _ in income_entries)
#     total_expense = sum(amount for amount, _ in expense_entries)
#     balance = total_income - total_expense
#     print(f"Current Balance: {balance:.2f} Baht")
#     return balance
#
# # ตัวอย่างการใช้งาน
# add_income(1000.0, "Salary")
# add_income(500.0, "Freelance")
# add_expense(150.0, "Groceries")
# add_expense(100.0, "Transport")
#
# print()
# display_income_entries()
# print()
# display_expense_entries()
# print()
# calculate_balance()

