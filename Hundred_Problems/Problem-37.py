# print a number pattern

def print_number_pattern(rows: int) -> None:
    n = ""
    for i in range(1,rows+1):
        n += str(i)
        print("-" * (rows-i) + n[::-1])

print_number_pattern(5)