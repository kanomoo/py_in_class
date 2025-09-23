# searchcountry names by staring letter

# def search_countries_by_letter(country_data: dict[str,str], letter: str) -> list[str]:
#     letter = letter.lower()
#     data = []
#     for k in country_data:
#         for v in country_data[k]:
#             v = v.lower()
#             if letter in v:
#                 data.append(country_data[k])
#     return data

def search_countries_by_letter(country_data: dict[str,str], letter: str) -> list[str]:
    letter = letter.lower()
    data = []
    for k in country_data:
        if letter == country_data[k][0].lower():
            data.append(country_data[k])
    return sorted(data) # เรียงตามตัวอักษรตามโจทย์


# def search_countries_by_letter(country_data: dict[str, str], letter: str) -> list[str]:
#     letter = letter.lower()
#     data = []
#     for country_name in country_data.values():  # ใช้ .values() เพื่อดึงชื่อประเทศ
#         if country_name.lower().startswith(letter):  # เช็คว่าเริ่มต้นด้วยตัวอักษรนั้นไหม
#             data.append(country_name)
#     return sorted(data)  # เรียงลำดับตามตัวอักษร


country_data = {
        "+1": "United States",
        "+44": "United Kingdom",
        "+91": "India",
        "+81": "Japan",
        "+49": "Germany",
        "+86": "China"
    }
letter = "U"
print(search_countries_by_letter(country_data, letter))