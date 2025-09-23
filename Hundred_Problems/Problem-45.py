# calculate annual rate of return

def calculate_annual_return(initial_investment: float, final_investment: float, years: int) -> float:
    A = (final_investment / initial_investment) ** (1/years) -1
    return round(A*100,2)

initial_investment = 1000
final_investment = 1500
years = 5
print(calculate_annual_return(initial_investment,final_investment,years))