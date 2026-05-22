# speeding violation detection and fine issuance

# def calculate_speeding_fine(speed: float, speed_limit: float) -> str:
#     limit = {160:2000,140:1500,120:1000,89:500}
#     for i in limit:
#         if speed > i:
#             return f"Fine: {limit[i]:,} Baht"
#     else:
#         return f"No fine."

# print(calculate_speeding_fine(141,0))

# def calculate_speeding_fine(speed: float, speed_limit: float) -> str:
#     limit = {160: 2000, 140: 1500, 120: 1000, 90: 500}
#     if speed <= speed_limit: return "No fine."
#     for l in limit:
#         if speed >= l: return f"Fine: {limit[l]} Baht"


def calculate_speeding_fine(speed: float, speed_limit: float = 0) -> str:
    limit = {160: 2000, 140: 1500, 120: 1000, 90: 500}
    if speed <= speed_limit: return "No fine."
    return next(f"Fine: {limit[l]} Bath"for l in limit if speed >= l)

if __name__ == "__main__":
    print(calculate_speeding_fine(141, 140))