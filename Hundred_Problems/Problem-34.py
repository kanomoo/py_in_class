# print a rectangle pattern

# def print_rectangle_pattern(rows: int, columns: int) -> None:
#     for i in range(rows):
#         print("*" * columns)

# print_rectangle_pattern(5,5)

def print_rectangle_pattern(rows: int, columns: int) -> None:
    for i in range(rows): print("*" * columns)
    
if __name__ == "__main__":
    print_rectangle_pattern(5,  5)