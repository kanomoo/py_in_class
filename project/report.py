from tabulate import tabulate
from collections import defaultdict
from datetime import datetime

COMMISSION_RATE = 0.05  # 5%

class ReportManager:
    def __init__(self, product_mgr, employee_mgr, sale_mgr):
        self.product_mgr = product_mgr
        self.employee_mgr = employee_mgr
        self.sale_mgr = sale_mgr

    def show_products(self):
        print("\n=== Product List ===")
        print(tabulate(self.product_mgr.products, headers="keys", tablefmt="fancy_grid"))

    def show_employees(self):
        print("\n=== Employee List ===")
        print(tabulate(self.employee_mgr.employees, headers="keys", tablefmt="fancy_grid"))

    def daily_sales(self):
        print("\n=== Daily Sales Summary ===")
        today = datetime.now().strftime("%Y-%m-%d")
        sales = [s for s in self.sale_mgr.sales if s["date"] == today]
        rows = []
        for s in sales:
            prod = next((p for p in self.product_mgr.products if p["id"] == s["product_id"]), None)
            if prod:
                rows.append({
                    "Product": prod["name"],
                    "Type": prod["type"],
                    "Qty": s["qty"],
                    "Total": float(prod["price"]) * int(s["qty"])
                })
        print(tabulate(rows, headers="keys", tablefmt="fancy_grid"))

    def sales_by_employee(self):
        print("\n=== Sales by Employee ===")
        emp_sales = defaultdict(float)
        for s in self.sale_mgr.sales:
            prod = next((p for p in self.product_mgr.products if p["id"] == s["product_id"]), None)
            if prod:
                emp_sales[s["employee_id"]] += float(prod["price"]) * int(s["qty"])
        rows = []
        for eid, total in emp_sales.items():
            emp = next((e for e in self.employee_mgr.employees if e["id"] == eid), {"name": eid})
            rows.append({"Employee": emp["name"], "Total Sales": total})
        print(tabulate(rows, headers="keys", tablefmt="fancy_grid"))

    def sales_by_product(self):
        print("\n=== Sales by Product ===")
        prod_sales = defaultdict(int)
        for s in self.sale_mgr.sales:
            prod_sales[s["product_id"]] += int(s["qty"])
        rows = []
        for pid, qty in prod_sales.items():
            prod = next((p for p in self.product_mgr.products if p["id"] == pid), {"name": pid, "type": ""})
            rows.append({"Product": prod["name"], "Type": prod["type"], "Total Sold": qty})
        print(tabulate(rows, headers="keys", tablefmt="fancy_grid"))

    def employee_commission(self):
        print("\n=== Employee Commission ===")
        emp_sales = defaultdict(float)
        for s in self.sale_mgr.sales:
            prod = next((p for p in self.product_mgr.products if p["id"] == s["product_id"]), None)
            if prod:
                emp_sales[s["employee_id"]] += float(prod["price"]) * int(s["qty"])
        rows = []
        for eid, total in emp_sales.items():
            emp = next((e for e in self.employee_mgr.employees if e["id"] == eid), {"name": eid})
            commission = total * COMMISSION_RATE
            rows.append({"Employee": emp["name"], "Total Sales": total, "Commission": commission})
        print(tabulate(rows, headers="keys", tablefmt="fancy_grid"))
