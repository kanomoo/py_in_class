# convert temperature between fahrenheit and celsius

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    celsius = (fahrenheit - 32) * 5/9
    return celsius
def celsius_to_fahrenheit(celsius: float) -> float:
    fahrenheit = (celsius * (9/5) + 32)
    return fahrenheit

print(fahrenheit_to_celsius(32))
print(celsius_to_fahrenheit(100))
