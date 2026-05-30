# K-partition subset sum

# def can_partition_k_subsets(nums: list, k: int) -> bool:
#     nums_list = []
#     Max = max(nums)
#     nums.remove(Max)
#     nums_list.append([Max])
#     nums = sorted(nums)
#     for i in range(len(nums) // 2):
#         first, second = nums[i], nums[len(nums) - (i + 1)]
#         if first == second: break
#         if first + second == Max: nums_list.append([first, second])
#     return k == len(nums_list)

# def can_partition_k_subsets(nums: list, k: int) -> bool:
#     dp, Max = [], max(nums)
#     dp.append([Max])
#     nums.remove(Max)
#     def k_subsets(nums: list, k: int):
#         if len(nums) <= 1: return k == len(dp)
#         min_nums , max_nums = max(nums), min(nums)
#         if max_nums + min_nums == Max:
#             dp.append([max_nums, min_nums])
#             nums.remove(max_nums)
#             nums.remove(min_nums)
#         k_subsets(nums, k)
#     return k_subsets(nums, k)

# def can_partition_k_subsets(nums: list, k: int) -> bool:
#     dp, Max = [], max(nums)
#     dp.append([Max])
#     nums.remove(Max)
#     def k_subsets(nums: list, k: int):
#         if len(nums) > 1:
#             min_nums , max_nums = max(nums), min(nums)
#             if max_nums + min_nums == Max:
#                 dp.append([max_nums, min_nums])
#                 nums.remove(max_nums)
#                 nums.remove(min_nums)
#             k_subsets(nums, k)
#         return k == len(dp)
#     return k_subsets(nums, k)

# def can_partition_k_subsets(nums: list, k: int) -> bool:
#     if sum(nums) % k == 0 : return True
#     return False

# def can_partition_k_subsets(nums: list, k: int):
#     if sum(nums) % k != 0: return False  # ตรวจสอบว่า ผลรวมทั้งหมดหารด้วย k ลงตัวหรือไม่ ถ้าไม่ลงตัว แปลว่าแบ่งเป็น k กลุ่มที่มีผลรวมเท่ากันไม่ได้แน่นอน
#     nums.sort(reverse = True) # ทำแบบนี้เพื่อช่วยให้ backtracking ทำงานเร็วขึ้น ช่วยลดจำนวนกรณีที่ต้องลอง
#     target = sum(nums) // k # target คือผลรวมของ subset
#     used = [False] * len(nums) #สร้างลิสต์ไว้เก็บว่าเลขแต่ละตัวถูกใช้ไปแล้วหรือยัง
#     def backtrack(i, k, subsetSum):
# สร้างฟังก์ชัน recursive สำหรับลองจัดกลุ่ม
# พารามิเตอร์:
# i = ตำแหน่งเริ่มต้นที่ใช้ลองเลือกตัวเลข
# k = จำนวนกลุ่มที่ยังต้องสร้าง
# subsetSum = ผลรวมปัจจุบันของกลุ่มที่กำลังเติมอยู่
#         if k == 0: return True
#         if subsetSum == target: return backtrack(0, k - 1, 0)
#         for j in range(i, len(nums)):
#             if used[j] or subsetSum + nums[j] > target: continue
#             used[j] = True
#             if backtrack(j + 1, k, subsetSum + nums[j]): return True
#             used[j] = False
#         return False
#     return backtrack(0, k, 0)


# def can_partition_k_subsets(nums: list, k: int):
#     if sum(nums) % k != 0: return False
#     nums.sort(reverse = True)
#     target = sum(nums) // k
#     used = [False] * len(nums)
#     def backtrack(i, k, subsetSum):
#         if k == 0: return True
#         if subsetSum == target: return backtrack(0, k - 1, 0)
#         for j in range(i, len(nums)):
#             if used[j] or subsetSum + nums[j] > target: continue
#             used[j] = True
#             if backtrack(j + 1, k, subsetSum + nums[j]): return True
#             used[j] = False
#         return False
#     return backtrack(0, k, 0)


def can_partition_k_subsets(nums: list, k: int):
    if sum(nums) % k != 0: return False
    nums.sort(reverse = True)
    target = sum(nums) // k
    used = [False] * len(nums)
    def backtrack(i, k, subsetSum):
        if k == 0: return True
        if subsetSum == target: return backtrack(0, k - 1, 0)
        for j in range(i, len(nums)):
            if used[j] or subsetSum + nums[j] > target: continue
            used[j] = True
            if backtrack(j + 1, k, subsetSum + nums[j]): return True
            used[j] = False
        return False
    return backtrack(0, k, 0)



if __name__ == "__main__":
    print(can_partition_k_subsets([4, 3, 2, 3, 5, 2, 1], 4))
    print(can_partition_k_subsets([1, 2, 3, 4], 3))