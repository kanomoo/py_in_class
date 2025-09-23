# separate even and odd numbers

def separate_even_odd(numbers: list[int]) -> tuple[list[int], list[int]]:
    even, odd = [], []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(separate_even_odd(numbers))