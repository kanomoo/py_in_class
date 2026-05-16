# divisor finder
# def find_divisors(n: int) -> list[int]:
#     data = []
#     for i in range(1,n+1):
#         if n % i == 0: data.append(i)
#     return data

# print(find_divisors(20))

def find_divisors(n: int) -> list[int]:
    num_divisors = []
    if n >= 1 and n <= 1000:
        for i in range(1, n + 1):
            if n % i == 0: num_divisors.append(i)
    return num_divisors

if __name__ == "__main__":
    print(find_divisors(20))