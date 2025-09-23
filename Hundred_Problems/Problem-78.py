# Cashier class for managing products

class Cashier:
    def __init__(self):
        self.data = {} #ให้.data เป็น dic

    def add_product(self, name: str, price: float, quantity: int):
        self.data[name] = price,quantity

    def remove_product(self, name: str):
        if name in self.data:
            del self.data[name] #del คำสั่งลบตัวแปร
            print(f"{name} removed.")
        else:
            print(f"{name} not found.")

    def calculate_total(self) -> float:
        total = 0
        for k in self.data:
            total += self.data[k][0] * self.data[k][1]
        return total

    def display_products(self):
        for k in self.data:
            print(f"{k} - Price: ${self.data[k][0]}, Quantity: {self.data[k][1]}")

# cashier = Cashier()
# cashier.add_product("Apple",0.5,10)
# cashier.add_product("Banana",0.3,5)
# cashier.display_products()
# print("Total Cost: $",cashier.calculate_total(),sep="")
# print()
# cashier.remove_product("Banana")
# cashier.display_products()

cashier = Cashier()
while True:
    print("\nMenu Cashier\n\n1. Add a product.\n2. Remove a product.\n3. Calculate the total cost.\n4. Display all products\n5. Exit the program.\n")
    choice = int(input("Select choice : "))
    match choice:
        case 1:
            name = input("Enter name : ")
            price = float(input("Enter price : "))
            quantity = int(input("Enter quantity : "))
            cashier.add_product(name,price,quantity)
        case 2:
            remove = input("Enter product to remove : ")
            cashier.remove_product(remove)
        case 3:
            print("Total Cost: $",cashier.calculate_total(),sep="")
        case 4:
            cashier.display_products()
        case 5:
            print("Exit program.")
            break
        case _:
            print("No choice:")