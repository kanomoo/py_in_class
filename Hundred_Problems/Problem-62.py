# speeding violation detection and fine issuance

def calculate_speeding_fine(speed: float, speed_limit: float) -> str:
    limit = {160:2000,140:1500,120:1000,89:500}
    for i in limit:
        if speed > i:
            return f"Fine: {limit[i]:,} Baht"
    else:
        return f"No fine."

print(calculate_speeding_fine(141,0))