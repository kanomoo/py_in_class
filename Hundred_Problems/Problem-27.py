# build a set with user input

def build_set() -> set[int]:
    nums = set()
    while len(nums) < 5:
        num = int(input("Enter : "))
        if num in nums:
            print("Please input unique")
        nums.add(num)
    return nums

print(build_set())