# convert temperature between fahrenheit and celsius

# def fahrenheit_to_celsius(fahrenheit: float) -> float:
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius
# def celsius_to_fahrenheit(celsius: float) -> float:
#     fahrenheit = (celsius * (9/5) + 32)
#     return fahrenheit

# print(fahrenheit_to_celsius(32))
# print(celsius_to_fahrenheit(100))


# class Temperature:
#     def __init__(self):
#         pass

#     def fahrenheit_to_celsius(fahrenheit: float) -> float:
#         return (fahrenheit - 32) * 5 / 9

#     def celsius_to_fahrenheit(celsius: float) -> float:
#         return( celsius * 9 / 5) + 32

# print(Temperature.fahrenheit_to_celsius(32))
# print(Temperature.celsius_to_fahrenheit(100))



# class Temperature:
#     def __init__(self):
#         pass

#     def fahrenheit_to_celsius(self, fahrenheit: float) -> float:
#         return (fahrenheit - 32) * 5 / 9

#     def celsius_to_fahrenheit(self, celsius: float) -> float:
#         return( celsius * 9 / 5) + 32

# t = Temperature()

# print(t.fahrenheit_to_celsius(32), t.celsius_to_fahrenheit(100), sep = "\n")


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32

if __name__ == "__main__":
    print(fahrenheit_to_celsius(32))
    print(celsius_to_fahrenheit(100))