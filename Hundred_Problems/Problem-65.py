# calculate term gpa based on grades

# def calculate_gpa(grades: list[int]) -> float:
#     grade = {80:4,75:3.5,70:3,65:2.5,60:2,55:1.5,50:1,0:0}
#     data = []
#     for i in grades:
#         for k, v in grade.items():
#             if i >= k:
#                 data.append(v)
#                 break
#     return sum(data) / len(data)

# print(calculate_gpa([85,72,63,58,49]))


def calculate_gpa(grades: list[int]) -> float:
    grade_points, points = {80: 4, 75: 3.5, 70: 3, 65: 2.5, 60: 2.0, 55: 1.5, 50: 1, 0: 0}, []
    points = [next(grade_points[g] for g in grade_points if p >= g) for p in grades]
    return sum(points) / len(grades)

if __name__ == "__main__":
    grades = [85, 72, 63, 58, 49]
    print(calculate_gpa(grades))