# calculate squares and statistics

# def calculate_statistics(t: tuple[int, ...]) -> tuple[tuple[int, ...], int, int, int ,float]:
#     value = ()
#     for i in t:
#         value += (i**2,)
#     Max = max(value)
#     Min = min(value)
#     total = sum(value)
#     avg = total / len(value)
#     value = ((value),Max, Min, total, avg)
#     return value

# t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(calculate_statistics(t))

import math

def calculate_statistics(t: tuple[int, ...]) -> tuple[tuple[int, ...], int, int, int, float]:
    squared_statistics = tuple(i ** 2 for i in t)
    max_statistics, min_statistics, sum_statistics = max(squared_statistics), min(squared_statistics), sum(squared_statistics)
    average_statistics = sum_statistics / len(squared_statistics)
    return (squared_statistics, max_statistics, min_statistics, sum_statistics, average_statistics)

if __name__ == "__main__":
    statistics = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(calculate_statistics(statistics))