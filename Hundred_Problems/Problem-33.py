# median calculation

# def calculate_median(provinces: dict[str, int]) -> list[tuple[str, int | float]] | None:
#     data = []
#     for i in provinces:
#         data.append(provinces[i])
#     data.sort()
#     n = len(data)
#     mid = n // 2
#
#     if n % 2 != 0: median = data[mid]
#     else: median = data[mid - 1] + data[mid] / 2
#
#     for n in provinces:
#         if median == provinces[n]:
#             return [(n,median)]



# def calculate_median(provinces: dict[str, int]) -> list[tuple[str, int]]:
#     values = sorted(provinces.values()) # sorted(...) เป็นฟังก์ชันที่ใช้ เรียงลำดับข้อมูลจากน้อยไปมาก  .value จะดึงเฉพาะ ค่าของ value จาก dictionary
#     n = len(values)
#
#     if n % 2 == 1:
#         median = values[n // 2]
#     else:
#         median = (values[n // 2 -1 ] + values[n // 2]) /2
#
#     result = []
#     for country, count in provinces.items(): # .items() ที่ใช้คืนค่าเป็น คู่ของ key และ value ทั้งหมดในรูปแบบ tuple คืนค่า: (''Thailand', 76) สามารถใช้ for 2 ค่าได้
#         if count == median:
#             result.append((country, count))
#
#     return  result

def calculate_median(provinces: dict[str, int]) -> list[tuple[str, int]]:
    value = sorted(provinces.values())
    n = len(value)
    if n % 2 != 0:
        median = value[n // 2]
    else:
        median = value[n // 2 - 1] + value[n // 2] / 2
    result = []
    for k,v in provinces.items():
        if median == v:
            result.append((k,v))
    return result

# ตัวอย่างการใช้งาน
data = {'Thailand': 76, 'Laos': 17, 'Vietnam': 58, 'Japan': 47, 'China': 23}
print(calculate_median(data))
