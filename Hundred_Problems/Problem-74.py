# car class

class Car:
    def __init__(self, brand: str, model: str, year: int, color: str):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def display_details(self) -> None:
        print(f"Brand: {[self.brand]}\nModel: {[self.model]}\nYear: {[self.year]}\nColor: {[self.color]}")

car = Car("Toyota","Camry",2022,"Blue")
car.display_details()

while True:
    print("\nCreate a new car\n\n1. Create a new car\n2. Display car details\n3. Exit")
    choice = input("Select choice : ")
    match choice:
        case "1":
            try:
                brand = input("Enter brand : ")
                model = input("Enter model : ")
                year = int(input("Enter year : "))
                color = input("Enter color :")
                car2 = Car(brand,model,year,color)
            except:
                print("Please input year to integer")
        case "2":
            try:
                print()
                car2.display_details()
            except:
                print("Please create a new car")
        case "3":
            print("Exit Program")
            break
        case _:
            print("No choice")