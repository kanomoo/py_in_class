# accumulated investment calculation

def calculate_investment_growth(principal: float, annual_rate: float, years: int) -> list[float]:
    A = []
    for i in range(1,years+1):
        a = principal * ((1 + annual_rate / 100) ** i)
        A.append(round(a,2))
    return A

principal = 1000
annual_rate = 5
years = 5
print(calculate_investment_growth(principal, annual_rate, years))