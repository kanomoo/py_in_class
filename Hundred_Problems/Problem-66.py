# restaurant menu for egg dishes

def calculate_total_cost(fried_eggs: int, omelets: int, bolled_eggs: int) -> int:
    return (fried_eggs * 7) + (omelets * 10) + (bolled_eggs * 5)

print(calculate_total_cost(2,3,1))