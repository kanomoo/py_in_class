# Tree Class

class Tree:
    def __init__(self, species: str, height: float, age: int, location: str):
        self.species = species
        self.height = height
        self.age = age
        self.location = location

    def grow(self, growth_amount: float):
        self.height += growth_amount

    def change_location(self, new_location: str):
        self.location = new_location

    def display_info(self):
        print(f"plaintext\nCopy code\nSpecies: {self.species}\nHeight: {self.height}\n"
              f"Age: {self.age}\nLocation: {self.location}")
species = "Oak"
height = 5.0
age = 10
location = "Central Park"
tree = Tree(species,height,age,location)
tree.display_info()

print()
tree.grow(0.5)
tree.change_location("Botanical Garden")
tree.display_info()