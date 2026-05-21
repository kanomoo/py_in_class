# # calculate cumulative sum

# def cumulative_sum(n: int) -> int:
#     c = int(n * (n+1) / 2)
#     return c

# print(cumulative_sum(5))


def cumulative_sum(n: int) -> int:
    return n * (n + 1) / 2

if __name__ == "__main__":
    print(cumulative_sum(5))