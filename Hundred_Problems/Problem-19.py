def sum_matrices(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        matrix.append(row)
    return matrix

matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix2 = [[4,3,2,1],[4,3,2,1],[4,3,2,1]]
print(sum_matrices(matrix1, matrix2))