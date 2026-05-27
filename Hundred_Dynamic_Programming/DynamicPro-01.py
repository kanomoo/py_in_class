def fibo(n: int, memo: dict = None) -> int:
    if memo is None: memo = {}
    if n <= 1: return n
    if n in memo: return memo[n]
    memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
    return memo[n]



if __name__ == "__main__":
    print(fibo(10))