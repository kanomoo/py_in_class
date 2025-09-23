# K-partition subset sum

def can_partition_k_subsets(nums: list, k: int) -> bool:
    s = []
    nums.remove(max(nums))
    p = nums.pop(1)
    p += nums.pop(2)
    print(p)
    # for i in range(len(nums) // 2):
    #     pop

nums = [4,3,2,3,5,2,1]
k = 4
print(can_partition_k_subsets(nums,k))