# # calculate parking fee

# def calculate_parking_fee(hours: int, minutes: int) -> int:
#     if hours > 0:
#         hours -= 1
#     if minutes > 0:
#         hours += 1
#     return hours * 50
# print(calculate_parking_fee(2,30))

def calculate_parking_fee(hours: int, minutes: int) -> int:
    return (hours + (1 if minutes > 0 else 0) - 1) * 50

if __name__ == "__main__":
    hours, minutes = 2, 30
    print(calculate_parking_fee(hours, minutes))