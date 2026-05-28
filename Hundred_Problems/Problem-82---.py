# # recursive permutation finder

# def find_permutations(s: str) -> list:
#     # Base case: ถ้ายาว 1 ตัวอักษร ให้คืน [s]
#     if len(s) == 1:
#         return [s]
#
#     permutations = []
#
#     # Loop ทุกตัวในสตริง
#     for i in range(len(s)):
#         # ตัวอักษรที่เลือกไว้
#         char = s[i]
#         # สร้าง substring ที่เหลือโดยตัดตัวอักษรนั้นออก
#         remaining = s[:i] + s[i+1:]
#         # เรียก recursive เพื่อหาคำเรียงของ substring ที่เหลือ
#         for perm in find_permutations(remaining):
#             permutations.append(char + perm)
#
#     # คืนลิสต์ที่เรียงลำดับแล้ว
#     return sorted(permutations)

# def find_permutations(s: str) -> list:
#     if len(s) == 1:
#         return [s]
#     permutations = []
#     for i in range(len(s)):
#         char = s[i]
#         # print(char)
#         remaining = s[:i] + s[i+1:]  # :0 1: | :1 2: | :2 3: / | -  bc|  a c |  ab  -
#         # print(remaining) # bc # ac # ab
#         for perm in find_permutations(remaining): # bc # ac # ab
#             permutations.append(char + perm)
#
#     return permutations
#
# print(find_permutations("abc"))

# def find_permutations(s: str) -> list:
#     perm = list(permutations(s))
#     p = []
#     for i in perm:
#         p += ["".join(i)]
#     return p


from itertools import permutations

# def find_permutations(s: str) -> list:
#     perm = set(permutations("abc"))
#     p = ["".join(i) for i in perm]
#     return sorted(p)

# def find_permutations(s: str) -> list:
#     perm = list(permutations(s))
#     p = ["".join(i) for i in perm]
#     return p



# def find_permutations(s: str) -> list:
#     if len(s) == 1:
#         return [s]
#
#     permutations = []
#
#     for i in range(len(s)):
#         char = s[i]
#         remaining = s[:i] + s[i+1:]
#         for i in find_permutations(remaining):
#             permutations.append(char + i)
#     return permutations


# from itertools import permutations

# def find_permutations(s: str) -> list:
#     result = []
#     for i in permutations(s):
#         result.append("".join(i))
#     return result

# print(find_permutations("abc"))


# def find_permutations(s: str) -> list:
#     return ([[s[i] + s[i + 1 if i + 1 < 2 else i - 1] + s[i + 2 if (i + 2) < 3 else (i + 1) % 3] for i in range(len(s))],\
#         [s[i] + s[i + 2 if (i + 2) < 3 else (i + 1) % 3] + s[i + 1 if i + 1 < 2 else i - 1]  for i in range(len(s))]])

# if __name__ == "__main__":
#     print(find_permutations("abc"))


# def find_permutations(s: str) -> list:
#     if len(s) <= 1: return s
#     permutations = []
#     for i in range(len(s)):
#         char = s[i]
#         re = s[:i] + s[i + 1:]
#         for n in find_permutations(re):
#             permutations.append(char + n)
#     return sorted(permutations)
















def find_permutations(s: str) -> list:
    if len(s) == 1: return s
    permutations = []
    for i in range(len(s)):
        char, re = s[i], s[:i] + s[i + 1:]
        for n in find_permutations(re):
            permutations.append(char + n)
    return permutations

if __name__ == "__main__":
    print(find_permutations("abc"))