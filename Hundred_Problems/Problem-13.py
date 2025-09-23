#reverse characters of a string

# def reverse_string(s: str) -> str:
#     reversed_s = ""
#     for ch in s:
#         reversed_s = ch + reversed_s  # เติมด้านหน้า
#     return reversed_s

def reverse_string(s: str) -> str:
    return s[::-1]

print(reverse_string("Hello World"))