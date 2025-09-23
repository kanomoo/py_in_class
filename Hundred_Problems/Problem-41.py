# calculate discounted prices

def calculate_discounted_prices(prices: list[float], discount_percentage: float) -> list[float]:
    result = []
    for i in prices:
        i = i -  i * (discount_percentage / 100)
        result.append(i)
    return result

prices = [100.0, 250.0, 75.0]
discount_percentage = 20.0
print(calculate_discounted_prices(prices, discount_percentage))