# print a diamond pattern

def print_diamond_pattern(n: int) -> None:
    for i in range(n):
        print("*" * (i+1))
    for n in range(n,0,-1):
        print("*" * (n-1))

print_diamond_pattern(3)