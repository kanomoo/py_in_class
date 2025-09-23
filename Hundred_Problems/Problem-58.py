# find all divisors of a given number

def find_divisors(num: int) -> list:
    result = []
    for i in range(1,num+1):
        if num % i == 0:
            result.append(i)
    return result

print(find_divisors(12))