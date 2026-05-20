# calculate Profit from sales and costs

# def calculate_profit(sales: tuple[float, float, float, float, float], costs: tuple[float, float, float, float,
# float]) -> tuple[tuple[float, float, float, float, float], float]:
#     total = ()
#     for i in range(len(sales)):
#         total += (sales[i] - costs[i],)
#     return total,sum(total)

# sales = (10000.0, 15000.0, 20000.0, 25000.0, 30000.0)
# costs = (7000.0, 8000.0,9000.0, 11000.0, 12000.0)
# print(calculate_profit(sales,costs))

def calculate_profit(sales: tuple[float, float, float ,float, float], costs: tuple[float, float, float, float, float]) -> tuple[tuple[float, float, float, float, float], float]:
    profit = tuple((sale - const) for sale, const in zip(sales, costs))
    return profit, sum(profit)

if __name__ == "__main__":
    sales, costs = (10000.0, 15000.0, 20000.0, 25000.0, 30000.0), (7000.0, 8000.0, 9000.0, 11000, 12000.0)
    print(calculate_profit(sales, costs))