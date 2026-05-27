def calculate_factorial(n: int) -> int:
    if n < 0: raise ValueError("Factorial is not defined for negative number ")
    if n == 0 or n == 1: return 1
    return n * calculate_factorial(n - 1)

if __name__ == "__main__":
    print(calculate_factorial(-3))