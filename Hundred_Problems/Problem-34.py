# print a rectangle pattern

def print_rectangle_pattern(rows: int, columns: int) -> None:
    for i in range(rows):
        print("*" * columns)

print_rectangle_pattern(5,5)