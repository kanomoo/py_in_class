# def fibo(n: int, memo: dict = None) -> int:
#     if memo is None: memo = {}
#     if n <= 1: return n
#     if n in memo: return memo[n]
#     memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
#     return memo[n]


# def fibo(n :int, memo: dict = None) -> int:
#     if n <= 1: return n
#     if memo == None: memo = {}
#     if n in memo: return memo[n]
#     memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
#     return memo[n]

# def fibo(n : int) -> int:
#     memo = {0: 0, 1: 1}
#     def f(n: int) -> int:
#         if n in memo: return memo[n]
#         memo[n] = f(n - 1) + f(n - 2)
#         return memo[n]
#     return f(n)

## Recursive Backtracking
# def fibo(n: int) -> int:
#     if n <= 1: return n
#     return fibo(n - 1) + fibo(n - 2)

# #Top-Down DP
# def fibo(n: int) -> int:
#     memo = {0: 0, 1: 1}
#     def f(n: int) -> int:
#         if n in memo: return memo[n]
#         memo[n] = f(n - 1) + f(n - 2)
#         return memo[n]
#     return f(n)

## Bottom-Up df (tabulation)
# def fibo(n: int) -> int:
#     dp = [0, 1]
#     for i in range(2, n + 1):
#         new = dp[i - 2] + dp[i - 1]
#         dp.append(new)
#     return dp[n]

def fibo(n):
    if n < 2: return n
    prev, cur = 0, 1
    for i in range(2, n + 1):
        prev, cur = cur, cur + prev
    return cur

# 0 1 1 2 3 5
if __name__ == "__main__":
    print(fibo(10000))