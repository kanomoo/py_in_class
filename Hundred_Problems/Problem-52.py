# group numbers by unit digit

def group_by_unit_digit(numbers: list[int]) -> list[list[int]]:
    result = [[] for i in range(10)]
    for n in numbers:
        digit = n % 10
        result[digit].append(n)
    return result

numbers = [21, 34, 51, 23, 37, 44, 60, 11, 91, 99]
print(group_by_unit_digit(numbers))