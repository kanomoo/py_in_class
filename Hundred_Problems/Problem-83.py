# # optimal path in a weighted grid
#
#
# # def min_cost_path(grid: list) -> tuple:
# #     rows = len(grid)
# #     cols = len(grid[0])
# #
# #     # ตาราง dp สำหรับเก็บต้นทุนต่ำสุด
# #     dp = [[0] * cols for _ in range(rows)]
# #
# #     # ตารางสำหรับย้อนเส้นทาง
# #     path_trace = [[None] * cols for _ in range(rows)]
# #
# #     dp[0][0] = grid[0][0]  # จุดเริ่มต้น
# #
# #     # กรอกค่าในแถวแรก (เดินได้แค่จากซ้าย)
# #     for j in range(1, cols):
# #         dp[0][j] = dp[0][j-1] + grid[0][j]
# #         path_trace[0][j] = (0, j-1)
# #
# #     # กรอกค่าในคอลัมน์แรก (เดินได้แค่จากบน)
# #     for i in range(1, rows):
# #         dp[i][0] = dp[i-1][0] + grid[i][0]
# #         path_trace[i][0] = (i-1, 0)
# #
# #     # กรอกค่าที่เหลือ
# #     for i in range(1, rows):
# #         for j in range(1, cols):
# #             if dp[i-1][j] < dp[i][j-1]:
# #                 dp[i][j] = dp[i-1][j] + grid[i][j]
# #                 path_trace[i][j] = (i-1, j)
# #             else:
# #                 dp[i][j] = dp[i][j-1] + grid[i][j]
# #                 path_trace[i][j] = (i, j-1)
# #
# #     # ย้อนเส้นทาง
# #     path = []
# #     r, c = rows - 1, cols - 1
# #     while r is not None and c is not None:
# #         path.append((r, c))
# #         r, c = path_trace[r][c] if path_trace[r][c] else (None, None)
# #
# #     path.reverse()
# #
# #     return dp[rows-1][cols-1], path
#
#
# def min_cost_path(grid: list) -> tuple:
#     rows = len(grid)
#     cols = len(grid[0])
#
#     dp = [[0] * cols for _ in range(rows)]
#
#     path_trace = [[None] * cols for _ in range(rows)]
#
#     dp[0][0] = grid[0][0]  # จุดเริ่มต้น
#
#     for j in range(1, cols):
#         dp[0][j] = dp[0][j-1] + grid[0][j]
#         path_trace[0][j] = (0, j-1)
#
#     for i in range(1, rows):
#         dp[i][0] = dp[i-1][0] + grid[i][0]
#         path_trace[i][0] = (i-1, 0)
#
#     for i in range(1, rows):
#         for j in range(1, cols):
#             if dp[i-1][j] < dp[i][j-1]:
#                 dp[i][j] = dp[i-1][j] + grid[i][j]
#                 path_trace[i][j] = (i-1, j)
#             else:
#                 dp[i][j] = dp[i][j-1] + grid[i][j]
#                 path_trace[i][j] = (i, j-1)
#
#     path = []
#     r, c = rows - 1, cols - 1
#     while r is not None and c is not None:
#         path.append((r, c))
#         r, c = path_trace[r][c] if path_trace[r][c] else (None, None)
#
#     path.reverse()
#
#     return dp[rows-1][cols-1], path
#
# grid = [ [1, 3, 1],
# [1, 5, 1],
# [4, 2, 1] ]
# print(min_cost_path(grid))

def min_cost_path(grid :list) -> int:
    result = sum(grid[0])
    for i in range(1,len(grid)):
        result += grid[i][-1]
    return result

# grid = [ [1, 3, 1],
# [1, 5, 1],
# [4, 2, 1] ]

grid = [[1, 2, 3],
[4, 8, 2],
[1, 5, 3]]

print(min_cost_path(grid))