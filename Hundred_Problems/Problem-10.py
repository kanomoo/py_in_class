#charater frequency count in multiple strings

# def character_frequency(*arge: str) -> dict: #*arge: str:  * รับอาร์กิวเมนต์หลายตัว
#     data,datas = {}, []
#     for n in arge:
#         for i in n:
#             datas.append(i)
#             data[i] = datas.count(i)
#     return data

def character_frequency(*arge: str) -> dict:
    if len(arge) == 5:
        data = {}
        for l in arge:
            for c in l:
                t_arge = "".join(arge)
                data[c] = t_arge.count(c)
        return data

print(character_frequency("hello", "world", "test", "case", "example"))
