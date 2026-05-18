#reverse characters of a string

# def reverse_string(s: str) -> str:
#     reversed_s = ""
#     for ch in s:
#         reversed_s = ch + reversed_s  # เติมด้านหน้า
#     return reversed_s

# def reverse_string(s: str) -> str:
#     return s[::-1]

# print(reverse_string("Hello World"))



def reverse_string(s: str) -> str:
    if len(s) >= 1 and len(s) <= 100: return s[::-1]
    return "string out of length"

if __name__ == "__main__":
    print(reverse_string("Hello World"))