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

# def min_cost_path(grid :list) -> int:
#     result = sum(grid[0])
#     for i in range(1,len(grid)):
#         result += grid[i][-1]
#     return result

# # grid = [ [1, 3, 1],
# # [1, 5, 1],
# # [4, 2, 1] ]

# grid = [[1, 2, 3],
# [4, 8, 2],
# [1, 5, 3]]

# print(min_cost_path(grid))



# def min_cost_path(grid: list) -> int:
#     for row in grid:

# if __name__ == "__main__":
#     grid = [[1, 3, 1],
#             [1, 5, 1],
#             [4, 2, 1]]
#     print(min_cost_path(grid))


# # fibo O(2 ^ n) ใหญ่เกิน
# def fibonacci(n : int) -> int:
#     if n <= 1: return n
#     return fibonacci(n - 1) + fibonacci(n - 2)

# def fibo(n: int, memo: dict = None) -> int:
#     if memo is None: memo = {}
#     if n <= 1: return n
#     if n in memo: return memo[n]
#     memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
#     return memo[n]


# # แบบปกติ
# def min_cost_path(grid: list) -> int:
#     if not grid or not grid[0]: return 0
#     rows = len(grid)
#     cols = len(grid[0])
    
#     dp = [[0 for _ in range(cols)] for _ in range(rows)]
#     dp[0][0] = grid[0][0]

#     for c in range(1, cols): dp[0][c] = dp[0][c-1] + grid[0][c]
        
#     for r in range(1, rows): dp[r][0] = dp[r-1][0] + grid[r][0]
        
#     for r in range(1, rows):
#         for c in range(1, cols):
#             dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r][c]
            
#     return dp[rows-1][cols-1]


## O(rows x clos)
# def min_cost_path(grid: list) -> int:
#     if not grid or not grid[0]: return 0
#     rows = len(grid)
#     cols = len(grid[0])
#     dp = [[0] * cols for _ in range(rows)]
#     dp[0][0] = grid[0][0]
#     for c in range(1, cols): dp[0][c] = dp[0][c - 1] + grid[0][c]
#     for r in range(1, rows): dp[r][0] = dp[r - 1][0] + grid[r][0]
#     for r in range(1, rows):
#         for c in range(1, cols):
#             dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]
#     return dp[rows - 1][cols - 1]


## O(cols)
# def min_cost_path(grid: list[list[int]]) -> int:
#     if not grid or not grid[0]: return 0
#     rows, cols = len(grid), len(grid[0])
#     dp = [0] * cols
#     dp[0] = grid[0][0]
#     for c in range(1, cols): dp[c] = dp[c-1] + grid[0][c]
#     for r in range(1, rows):
#         dp[0] += grid[r][0]
#         for c in range(1, cols):
#             dp[c] = min(dp[c], dp[c-1]) + grid[r][c]
#     return dp[cols-1]



# def min_cost_path(grid: list) -> int:
#     if not grid or not grid[0]: return 0
#     rows, cols = len(grid), len(grid[0])
#     dp, dp[0][0] = [[0 for _ in range(cols)] for _ in range(rows)], grid[0][0]
#     for c in range(1, cols): dp[0][c] = dp[0][c - 1] + grid[0][c]
#     for r in range(1, rows): dp[r][0] = dp[r - 1][0] + grid[r][0]
#     for r in range(1, rows):
#         for c in range(1, cols):
#             dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]
#     return dp[rows - 1][cols - 1]


# def min_cost_path(grid: list) -> int:
#     if not grid or not grid[0]: return 0
#     rows, cols = len(grid), len(grid[0])
#     dp, dp[0] = [0] * cols, grid[0][0]
#     for c in range(1, cols): dp[c] = dp[c - 1] + grid[0][c]
#     for r in range(1, rows):
#         dp[0] += grid[r][0]
#         for c in range(1, cols):
#             dp[c] = min(dp[c], dp[c - 1]) + grid[r][c]
#     return dp[cols - 1]




# def min_cost_path(grid: list) -> int:
#     if not grid or not grid[0]: return 0
#     rows, cols = len(grid), len(grid[0])
#     dp, dp[0][0] = [[0] * cols for _ in range(rows)], grid[0][0]
#     for c in range(1, cols): dp[0][c] = dp[0][c - 1] + grid[0][c]
#     for r in range(1, rows): dp[r][0] = dp[r - 1][0] + grid[r][0]
#     for r in range(1, rows):
#         for c in range(1, cols):
#             dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]
#     return dp[rows - 1][cols - 1]


def min_cost_path(grid: list) -> int:
    if not grid or not grid[0]: return 0
    rows, cols = len(grid), len(grid[0])
    dp, dp[0] = [0] * cols, grid[0][0]
    for c in range(1, cols): dp[c] = dp[c - 1] + grid[0][c]
    for r in range(1, rows):
        dp[0] += grid[r][0]
        for c in range(1, cols):
            dp[c] = min(dp[c - 1], dp[c]) + grid[r][c]
    return dp[cols - 1]

if __name__ == "__main__":
    grid = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]
    
    # grid = [[1, 2, 3],
    #         [4, 8, 2],
    #         [1, 5, 3]]

    print(min_cost_path(grid))