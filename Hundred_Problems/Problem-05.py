# divisor finder
def find_divisors(n: int) -> list[int]:
    data = []
    for i in range(1,n+1):
        if n % i == 0: data.append(i)
    return data

print(find_divisors(20))