# replace specific characters in a string

# def replace_characters(s: str) -> str:
#     mess = ""
#     for i in s:
#         match i:
#             case "a" | "A": mess += "@" # | คือ or
#             case "l" | "L": mess += "1"
#             case "o" | "O": mess += "0"
#             case _: mess += i
#     return mess

def replace_characters(s: str) -> str:
    s = s.replace("a","@").replace("A","@")
    s = s.replace("l","1").replace("L","1")
    s = s.replace("o","0").replace("O","0")
    return s

print(replace_characters("HELLO WORLD"))