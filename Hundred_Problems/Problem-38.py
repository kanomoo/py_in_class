# simple calculator

def add(a: float, b: float) -> float:
    return a + b
def subtract(a: float, b: float) -> float:
    return a - b
def multiply(a: float, b: float) -> float:
    return a * b
def divide(a: float, b: float) -> float:
    try:
        return a / b
    except:
        return "None or raise an exception"

print(add(5,3),
subtract(5,3),
multiply(5,3),
divide(6,3),
divide(6,0)
,sep="\n")