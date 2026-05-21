# # group numbers by unit digit

# def group_by_unit_digit(numbers: list[int]) -> list[list[int]]:
#     result = [[] for i in range(10)]
#     for n in numbers:
#         digit = n % 10
#         result[digit].append(n)
#     return result

# numbers = [21, 34, 51, 23, 37, 44, 60, 11, 91, 99]
# print(group_by_unit_digit(numbers))

# def group_by_unit_digit(numbers: list[int]) -> list[list[int]]:
#     digits_list = [[] for i in range(10)]
#     [digits_list[i % 10].append(i) for i in numbers]
#     return digits_list

def group_by_unit_digit(numbers: list[int]) -> list[list[int]]:
    digits_list = [[] for _ in range(10)]
    for n in numbers: digits_list[n % 10].append(n)
    return digits_list

if __name__ == "__main__":
    numbers = [21, 34, 51, 23, 37, 44, 60, 11, 91, 99]
    print(group_by_unit_digit(numbers))