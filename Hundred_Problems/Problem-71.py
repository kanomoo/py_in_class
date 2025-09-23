# person class

class Person:
    def __init__(self,name: str, age: int):
        """
        Initialize a new Person instance with name and age.

        Parameters:
        name (str): The name of the person.
        age (int): The age of the person.
        """
        self.name = name #self ตัวแทนชื่อตัวแปรด้านนอก
        self.age = age

    def get_name(self) -> str:
        """
        Return the name of the person.

        Return:
        Str: The name of the person.
        """
        return self.name

    def get_age(self) -> int:
        """
        Return the age of the person.

        Returns:
        int: the age of the person.
        """
        return self.age

    def set_name(self, name: str) -> None:
        """
        Set the name of the person.

        Parameters:
        name (str): The new name of the person.
        """
        self.name = name

    def set_age(self, age: int) -> None:
        """
        Set the age of the person.

        Parameters:
        age (int): The new age of the person.
        """
        self.age = age


person = Person("Alice",30)

print(person.get_name())
print(person.get_age())

person.set_name("Bob")
person.set_age(35)

print(person.get_name())
print(person.get_age())