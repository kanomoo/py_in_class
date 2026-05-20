# # print a diamond pattern

# def print_diamond_pattern(n: int) -> None:
#     for i in range(n):
#         print("*" * (i+1))
#     for n in range(n,0,-1):
#         print("*" * (n-1))

# print_diamond_pattern(3)]


def print_diamond_pattern(n: int) -> None:
    for i in range(1, n + 1): print("*" * i)
    for j in range(n - 1, 0, -1): print("*" * j)

if __name__ == "__main__":
    print_diamond_pattern(3)