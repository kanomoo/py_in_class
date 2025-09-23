# calculate the total payment after applying discounts

def calculate_total_payment(num_bills: int, bills: list[float]) -> float:
    discount = {10000:0.2,5000:0.1,1000:0.05,0:0}
    for k in discount:
        if sum(bills) >= k:
            return sum(bills) - (sum(bills) * discount[k])

num_bills = 3
bills = [3000,4000,3500]
print(calculate_total_payment(num_bills, bills))