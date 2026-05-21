# accumulated investment calculation

# def calculate_investment_growth(principal: float, annual_rate: float, years: int) -> list[float]:
#     A = []
#     for i in range(1,years+1):
#         a = principal * ((1 + annual_rate / 100) ** i)
#         A.append(round(a,2))
#     return A

# principal = 1000
# annual_rate = 5
# years = 5
# print(calculate_investment_growth(principal, annual_rate, years))


def calculate_investment_growth(principal: float, annual_rate: float, years: int) -> list[float]:
    return [round(1000 * pow(1 + annual_rate / 100, i), 2) for i in range(1, year + 1)]

if __name__ == "__main__":
    principal, annual_rate, year = 1000, 5, 5
    print(calculate_investment_growth(principal, annual_rate, year))