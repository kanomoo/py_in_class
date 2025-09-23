import csv

PRODUCT_FILE = "products.csv"

class ProductManager:
    def __init__(self):
        self.products = []
        self.load()

    def load(self):
        self.products = []
        try:
            with open(PRODUCT_FILE, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.products.append(row)
        except FileNotFoundError:
            pass

    def save(self):
        with open(PRODUCT_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["id", "name", "type", "price"])
            writer.writeheader()
            writer.writerows(self.products)

    def menu(self):
        print("\n--- Product Management ---")
        print("1. Add Product")
        print("2. List Products")
        print("0. Back")
        choice = input("Select: ")
        if choice == "1":
            self.add_product()
        elif choice == "2":
            self.list_products()
        elif choice == "0":
            return

    def add_product(self):
        pid = input("Product ID: ")
        name = input("Name: ")
        ptype = input("Type (Drink/Bakery): ")
        price = input("Price: ")
        self.products.append({"id": pid, "name": name, "type": ptype, "price": price})
        self.save()
        print("Product added.")

    def list_products(self):
        from tabulate import tabulate
        print(tabulate(self.products, headers="keys", tablefmt="fancy_grid"))
