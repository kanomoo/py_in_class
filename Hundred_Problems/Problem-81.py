# Advanced string transformation

def advanced_string_transformation(s: str) -> str:
    s = s[::-1].split()
    s.reverse()
    s = " ".join(s)

    s = s.swapcase() #สลับตัวพิมพ์ใหญ่และพิมพ์เล็ก ในสตริง

    mess2 = ""
    rv = {"a":"e","e":"i","i":"o","o":"u","u":"a",
          "A":"E","E":"I","I":"O","O":"U","U":"A"}

    for i in s:
        if i not in rv.keys():
            mess2 += i
        if i in rv.keys():
            mess2 += rv[i]

    mess3 = ""
    n = 0
    for i in mess2:
        n += 1
        if n == 4:
            mess3 += "#"
            n = 0
        else:
            mess3 += i


    return mess3

print(advanced_string_transformation("Hello World"))


# def advanced_string_transformation(s: str) -> str:
#     s = s[::-1].split()
#     s.reverse()
#     s = " ".join(s)
#     print(s)
#     s = s.swapcase() #สลับตัวพิมพ์ใหญ่และพิมพ์เล็ก ในสตริง
#     print(s)
#
#     mess2 = ""
#     rv = {"a":"e","e":"i","i":"o","o":"u","u":"a",
#           "A":"E","E":"I","I":"O","O":"U","U":"A"}
#
#     for i in s:
#         if i not in rv.keys():
#             mess2 += i
#         if i in rv.keys():
#             mess2 += rv[i]
#     print(mess2)
#
#     mess3 = ""
#     n = 0
#     for i in mess2:
#         n += 1
#         if n == 4:
#             mess3 += "#"
#             n = 0
#         else:
#             mess3 += i
#     print(mess3)
#
#     return mess3
#
# print(advanced_string_transformation("Hello World"))


# def advanced_string_transformation(s: str) -> str:
#     # Step 1: Reverse characters in each word
#     words = s.split()
#     reversed_words = [word[::-1] for word in words]
#     s = ' '.join(reversed_words)
#
#     # Step 2: Swap case
#     s = s.swapcase()
#
#     # Step 3: Replace vowels
#     vowel_map = {
#         'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a',
#         'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'
#     }
#     s = ''.join(vowel_map[c] if c in vowel_map else c for c in s)
#
#     # Step 4: Add '#' after every 3 characters (excluding spaces)
#     result = ''
#     count = 0
#     for c in s:
#         result += c
#         if c != ' ':
#             count += 1
#             if count % 3 == 0:
#                 result += '#'
#     return result
#
# print(advanced_string_transformation("Hello World"))
