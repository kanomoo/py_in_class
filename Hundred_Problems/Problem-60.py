# calculate parking fee

def calculate_parking_fee(hours: int, minutes: int) -> int:
    if hours > 0:
        hours -= 1
    if minutes > 0:
        hours += 1
    return hours * 50
print(calculate_parking_fee(2,30))