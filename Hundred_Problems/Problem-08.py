#extract even/odd indexed characters

# def separate_by_index(s: str) -> tuple[str, str]:
#     even = odd = ""
#     for i in range(0,len(s),+2):
#         even += s[i]
#     for i in range(1,len(s),+2):
#         odd += s[i]
#     return even,odd
#
# print(separate_by_index("Hello World"))

def separate_by_index(s: str) -> tuple[str, str]:
    even = s[::2]
    odd = s[1::2]
    return even,odd

print(separate_by_index("Hello World"))