# # pet class for different animals

# class Pet:
#     def __init__(self,species: str, breed: str, color: str, name: str, height: float, weight: float):
#         self.species = species
#         self.breed = breed
#         self.color = color
#         self.name = name
#         self.height = height
#         self.weight = weight

#     def display_info(self):
#         print(f"Pet information:\nSpecies: {self.species}\nBreed: {self.breed}"
#               f"\nColor: {self.color}\nName: {self.name}\nHeight: {self.height} cm\nWeight: {self.weight} kg")

# # pet = Pet("Dog","Labrador","Yellow","buddy",60.5,25.3)
# # pet.display_info()


# print("Select type of animal\n1. Dog\n2. Cat\n3. Bird")
# choice = input("Select choice : ")
# match choice:
#     case "1":
#         species = "Dog"
#     case "2":
#         species = "Cat"
#     case "3":
#         species = "Bird"
# bred = input("Breed : ")
# color = input("Color : ")
# name = input("Name : ")
# height = float(input("Height : "))
# weight = float(input("Weight : "))
# pet = Pet(species,bred,color,name,height,weight)
# print()
# pet.display_info()


class Pet:
    def __init__(self, species: str, breed: str, color: str, name: str, height: float, weight: float):
        self.species, self.breed, self.color, self.name, self.height, self.weight = species, breed, color, name, height, weight
    
    def display_info(self):
        print(f"Pet Information:\nSpecies: {self.species}\nBreed: {self.breed}\nColor: {self.color}\nName: {self.name}\nHeight: {self.height}\nWeight: {self.weight}")

def menu():
    while True:
        select = input("1. Create pet information\n2. Display pet details\n3. Exit\nSelect: "); print()
        match select:
            case "1":
                pet_type = input("1. Dog\n2. Cat\n3. Bird\nEnter pet type: ")
                match pet_type:
                    case "1": species = "Dog"
                    case "2": species = "Cat"
                    case "3": species = "Bird"
                    case "_": print("No choice.")
                pet = Pet(species, input("Enter breed: "), input("Enter Color: "), input("Enter name: "), float(input("Enter height: ")), float(input("Enter weight: ")))
                print()
            case "2": pet.display_info(); print()
            case "3": print("Exit Program.", end = ""); exit()
            case _: print("No choice.")

if __name__ == "__main__":
    menu()