# Transpose a matrix

# def transpose_matrix(matrix1: list[list[int]]) -> list[list[int]]:
#     matrix = []  # สร้างเมทริกซ์เปล่าไว้ใส่ผลลัพธ์
#     for i in range(len(matrix1[0])):  # วนตามจำนวนคอลัมน์ (กลายเป็นจำนวนแถวใหม่)
#         row = []
#         for j in range(len(matrix1)):  # วนตามจำนวนแถว (กลายเป็นจำนวนคอลัมน์ใหม่)
#             row.append(matrix1[j][i])  # ดึงค่า (j,i) มาใส่ตำแหน่ง (i,j) ใหม่
#         matrix.append(row)
#     return matrix


# def transpose_matrix(matrix1: list[list[int]]) -> list[list[int]]:
#     matrix = []
#     for i in range(len(matrix1[0])):
#         row = []
#         for j in range(len(matrix1)):
#             row.append(matrix1[j][i])
#         matrix.append(row)
#     return matrix

# matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print(transpose_matrix(matrix1))


# def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
#     transpose_list = []
#     for i in range(len(matrix[0])):
#         matrix_list = []
#         for j in range(len(matrix)):
#             matrix_list.append(matrix[j][i])
#         transpose_list.append(matrix_list)
#     return transpose_list


# def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
#     return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix)]

if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(transpose_matrix(matrix))