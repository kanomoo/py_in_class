# calculate term gpa based on grades

def calculate_gpa(grades: list[int]) -> float:
    grade = {80:4,75:3.5,70:3,65:2.5,60:2,55:1.5,50:1,0:0}
    data = []
    for i in grades:
        for k, v in grade.items():
            if i >= k:
                data.append(v)
                break
    return sum(data) / len(data)

print(calculate_gpa([85,72,63,58,49]))