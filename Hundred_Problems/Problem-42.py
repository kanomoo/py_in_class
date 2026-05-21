# frog jump calculation

# def calculate_jumps(d: int, s: int) -> int:
#     jump = 0
#     while True:
#         if s * jump < d:
#             jump += 1
#         else:
#             break
#     return jump

# # def calculate_jumps(d: int, s: int) -> int:
# #     return (d + s - 1) // s


# print(calculate_jumps(20,7))

def calculate_jumps(d: int, s: int) -> int:
    jump = 0
    while d > -1: d, jump = (d - s), (jump + 1)
    return jump

if __name__ == "__main__":
    print(calculate_jumps(21, 7))