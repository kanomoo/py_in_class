# # Cashier class for managing products

# class Cashier:
#     def __init__(self):
#         self.data = {} #ให้.data เป็น dic

#     def add_product(self, name: str, price: float, quantity: int):
#         self.data[name] = price,quantity

#     def remove_product(self, name: str):
#         if name in self.data:
#             del self.data[name] #del คำสั่งลบตัวแปร
#             print(f"{name} removed.")
#         else:
#             print(f"{name} not found.")

#     def calculate_total(self) -> float:
#         total = 0
#         for k in self.data:
#             total += self.data[k][0] * self.data[k][1]
#         return total

#     def display_products(self):
#         for k in self.data:
#             print(f"{k} - Price: ${self.data[k][0]}, Quantity: {self.data[k][1]}")

# # cashier = Cashier()
# # cashier.add_product("Apple",0.5,10)
# # cashier.add_product("Banana",0.3,5)
# # cashier.display_products()
# # print("Total Cost: $",cashier.calculate_total(),sep="")
# # print()
# # cashier.remove_product("Banana")
# # cashier.display_products()

# cashier = Cashier()
# while True:
#     print("\nMenu Cashier\n\n1. Add a product.\n2. Remove a product.\n3. Calculate the total cost.\n4. Display all products\n5. Exit the program.\n")
#     choice = int(input("Select choice : "))
#     match choice:
#         case 1:
#             name = input("Enter name : ")
#             price = float(input("Enter price : "))
#             quantity = int(input("Enter quantity : "))
#             cashier.add_product(name,price,quantity)
#         case 2:
#             remove = input("Enter product to remove : ")
#             cashier.remove_product(remove)
#         case 3:
#             print("Total Cost: $",cashier.calculate_total(),sep="")
#         case 4:
#             cashier.display_products()
#         case 5:
#             print("Exit program.")
#             break
#         case _:
#             print("No choice:")

# class Cashier:
#     def __init__(self):
#         self.product = {}

#     def add_product(self, name: str, price: float, quantity: int):
#         self.product[name] = {"price": price, "quantity": quantity}

#     def remove_product(self, name: str):
#         if name in self.product: self.product.pop(name); print("Remove success.")
#         else: print("No name in product.")

#     def calculate_total(self) -> float:
#         total = 0
#         for key in self.product:
#             price = 1
#             for v in self.product[key].values(): price *= v
#             total += price
#         return total

#     def display_products(self):
#         output = ""
#         "".title()
#         for key in self.product:
#             output += f"{key} - "
#             for k, v in self.product[key].items():
#                 if k == "price": output += f"{k.title()}: ${v}, "
#                 else: output += f"{k.title()}: {v}"
#             output += "\n"
#         output += f"Total Cost: ${self.calculate_total()}"
#         print(output)

# if __name__ == "__main__":
#     cashier = Cashier()
#     while True:
#         select = input("1. Add a product.\n2. Remove a product.\n3. Calculate the total cost.\n4. Display all products.\n5. Exit the program.\nSelect: ")
#         match select:
#             case "1": cashier.add_product(input("\nEnter name: "), float(input("Enter price: ")), float(input("Enter quantity: ")))
#             case "2": cashier.remove_product(input("\nEnter name: "))
#             case "3": print("\nTotal cost: " + str(cashier.calculate_total()))
#             case "4": print(); cashier.display_products()
#             case "5": print("\nExit program.", end = ""); exit()
#             case _: print("\nNo choice.")
#         print()


class Cashier:
    def __init__(self):
        self.products: dict[str, dict[str, float]] = {}

    def add_product(self, name: str, price: float, quantity: int):
        self.products[name] = {"price": price, "quantity": quantity}

    def remove_product(self, name: str):
        if name in self.products: self.products.pop(name); print("Remove success.")
        else: print("No name in product.")

    def calculate_total(self) -> float:
        return sum(info["price"] * info["quantity"] for info in self.products.values())

    def display_products(self):
        lines = [f"{name} - Price: ${info["price"]}, Quantity: {int(info["quantity"])}" for name, info in self.products.items()]
        print("\n".join(lines) + f"\nTotal Cost: {self.calculate_total()}")

if __name__ == "__main__":
    cashier = Cashier()
    while True:
        select = input("1. Add a product.\n2. Remove a product.\n3. Calculate the total cost.\n4. Display all products.\n5. Exit the program.\nSelect: ")
        match select:
            case "1": cashier.add_product(input("\nEnter name: "), float(input("Enter price: ")), float(input("Enter quantity: ")))
            case "2": cashier.remove_product(input("\nEnter name: "))
            case "3": print("\nTotal cost: " + str(cashier.calculate_total()))
            case "4": print(); cashier.display_products()
            case "5": print("\nExit program.", end = ""); exit()
            case _: print("\nNo choice.")
        print()