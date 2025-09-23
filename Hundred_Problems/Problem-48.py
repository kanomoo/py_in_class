# calculate cumulative sum

def cumulative_sum(n: int) -> int:
    c = int(n * (n+1) / 2)
    return c

print(cumulative_sum(5))