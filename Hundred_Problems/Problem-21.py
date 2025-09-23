# calculate squares and statistics

def calculate_statistics(t: tuple[int, ...]) -> tuple[tuple[int, ...], int, int, int ,float]:
    value = ()
    for i in t:
        value += (i**2,)
    Max = max(value)
    Min = min(value)
    total = sum(value)
    avg = total / len(value)
    value = ((value),Max, Min, total, avg)
    return value

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(calculate_statistics(t))