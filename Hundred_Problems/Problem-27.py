# build a set with user input

# def build_set() -> set[int]:
#     nums = set()
#     while len(nums) < 5:
#         num = int(input("Enter : "))
#         if num in nums:
#             print("Please input unique")
#         nums.add(num)
#     return nums

# print(build_set())

def build_set() -> set[int]:
    num_set = set()
    while (len(num_set)) < 5:
        num = input("Enter Number: ")
        num_set.add(num) if num not in num_set else print("unique integers.")
    return num_set

if __name__ == "__main__":
    print(build_set())