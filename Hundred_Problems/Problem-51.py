# # separate even and odd numbers

# def separate_even_odd(numbers: list[int]) -> tuple[list[int], list[int]]:
#     even, odd = [], []
#     for i in numbers:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     return even,odd

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(separate_even_odd(numbers))

# def separate_even_odd(numbers: list[int]) -> tuple[list[int], list[int]]:
#     return ([n for n in numbers if n % 2 == 0], [n for n in numbers if n % 2 != 0])

def separate_even_odd(numbers: list[int]) -> tuple[list[int], list[int]]:
    even, odd = [], []
    for n in numbers: (even if n % 2 == 0 else odd).append(n)
    return even, odd

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(separate_even_odd(numbers))