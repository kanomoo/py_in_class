import csv
from datetime import datetime

SALE_FILE = "sales.csv"

class SaleManager:
    def __init__(self):
        self.sales = []
        self.load()

    def load(self):
        self.sales = []
        try:
            with open(SALE_FILE, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.sales.append(row)
        except FileNotFoundError:
            pass

    def save(self):
        with open(SALE_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["date", "employee_id", "product_id", "qty"])
            writer.writeheader()
            writer.writerows(self.sales)

    def menu(self, product_mgr, employee_mgr):
        print("\n--- Record Sale ---")
        date = datetime.now().strftime("%Y-%m-%d")
        employee_id = input("Employee ID: ")
        product_id = input("Product ID: ")
        qty = input("Quantity: ")
        self.sales.append({
            "date": date,
            "employee_id": employee_id,
            "product_id": product_id,
            "qty": qty
        })
        self.save()
        print("Sale recorded.")
