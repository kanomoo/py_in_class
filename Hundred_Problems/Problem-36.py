# print a diamond pattern with hyphens

def print_diamond_pattern(n: int) -> None:
    n = n // 2
    for i in range(n):
        print("*" * ((n)-i) + "-" * i + "-" * i +"*" * ((n)-i))
    for j in range(2,n+1):
        print("*" * (j) + "-" * (n-j) + "-" * (n-j) + "*" * (j))


# def print_diamond_pattern(n: int) -> None:
#     half = n // 2
#     for i in range(half):
#         stars = '*' * (half - i)
#         hyphens = '-' * (i * 2)
#         print(stars + hyphens + stars)
#     # แถวกลาง
#     hyphens = '-' * (n - 2)
#     print('*' + hyphens + '*')
#
#     for i in range(half - 1, -1, -1):
#         stars = '*' * (half - i)
#         hyphens = '-' * (i * 2)
#         print(stars + hyphens + stars)


print_diamond_pattern(10)