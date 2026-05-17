#charater frequency count in multiple strings

# def character_frequency(*arge: str) -> dict: #*arge: str:  * รับอาร์กิวเมนต์หลายตัว
#     data,datas = {}, []
#     for n in arge:
#         for i in n:
#             datas.append(i)
#             data[i] = datas.count(i)
#     return data

# def character_frequency(*arge: str) -> dict:
#     if len(arge) == 5:
#         data = {}
#         for l in arge:
#             for c in l:
#                 t_arge = "".join(arge)
#                 data[c] = t_arge.count(c)
#         return data

# print(character_frequency("hello", "world", "test", "case", "example"))



# def character_frequency(*args: str) -> dict:
#     char_dict, char_list = {}, []
#     for i in args:
#         if len(i) >= 1 and len(i) <= 50:
#             for char in i:
#                 char_dict[char] = char_dict.get(char, 0) + 1 #ถ้ายังไม่เคยเจอให้คืนค่าเป็น None แต่โดนกำหนดใน parameter ที่ 2 ให้คืนค่าเป็น 0 โดนจะเก็บเป็น value ใน key คือสร้างข้อมูลใหม่เป็น 0 แต่ถ้าเเจอให้คืนค่า key และ + 1
#         else: return
#     return char_dict

# if __name__ == "__main__":
#     print(character_frequency("test"))


def character_frequency(*args: str) -> dict:
    char_dict = {}
    for text in args:
        if len(text) >= 1 and len(text) <= 50:
            for char in text: char_dict[char] = char_dict.get(char, 0) + 1
        else: return "char out of length"
    return char_dict


if __name__ == "__main__":
    print(character_frequency(""))