#medain calculation

def calculate_median(lst: list[int]) -> float:
    lst.sort()
    n = len(lst)
    mid = n // 2 # ตัดเศษ
    if n % 2 != 0:
        lst = float(lst[mid]) # ถ้าเป็นจำนวนเลขคี่
    else:
        lst = (lst[mid - 1] + lst[mid]) / 2 # ถ้าเป็นเลขคู่
    return lst

lst = [8, 4, 7, 4, 6, 2, 10, 9, 3, 7, 1]
print(calculate_median(lst))