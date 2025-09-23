# store student information in a dictionary

# def store_student_info(student_data: list[tuple[str,str]]) -> dict[str, str]:
#     d = {}
#     for i in student_data:
#         d[i[0]] = i[1]
#     return d

def store_student_info(student_data: list[tuple[str,str]]) -> dict[str, str]:
    return dict(student_data)

student_data = [("123456","Alice"),("654321","Bob"),("112233","charlie")]
print(store_student_info(student_data))