# def calculate_factorial(n: int) -> int:
#     if n < 0: raise ValueError("Factorial is not defined for negative number ")
#     if n == 0 or n == 1: return 1
#     return n * calculate_factorial(n - 1)

# def calculate_factorial(n: int) -> int:
#     if n in (0, 1): return 1
#     return n * calculate_factorial(n - 1)

# ไม่เสี่ยง stack overflow
def calculate_factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1): result *= i
    return result

if __name__ == "__main__":
    print(calculate_factorial(5))