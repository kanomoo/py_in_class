# toggle case of characters in a string

def toggle_case(s: str) -> str:
    mess = ""
    for i in s:
        if  i.islower(): # ใช้ islower แทน i == i.lower ได้
            i = i.upper()
        else:
            i = i.lower()
        mess += i
    return mess

print(toggle_case("Hello World!"))