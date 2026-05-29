# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if nums[i] + nums[j] == target and i != j: return [i, j]

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         nums_dict = {}
#         for i, v in enumerate(nums):
#             pair = target - v
#             if nums_dict.get(pair) != None: return[nums_dict.get(pair), i]
#             else: nums_dict[v] = i

# Top-Down DP
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         nums_dict = {}
#         for i in range(len(nums)):
#             if target - nums[i] in nums_dict: return [nums_dict[target - nums[i]], i]
#             if nums[i] not in nums_dict: nums_dict[nums[i]] = i

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         nums_dict = {}
#         for i, v in enumerate(nums):
#             pair = target - v
#             if pair in nums_dict: return [nums_dict.get(pair), i]
#             nums_dict[v] = i







# ใช้หลักการ top down memo สร้าง dict หรือ hash map เพื่อเก็บข้อมูล ถ้า loop ใน nums เมื่อ target - value ไม่มีใน
# nums_dict ให้สร้าง nums_dcit[v] = i (target คือจำนวนที่ต้องหา ถ้าเอา target - v ก็จะหาคู่ของ value ของมันเจอ target = pair + v)
# แล้วก็ return nums_dcit[pair], i (nums_dict[pair] คือ index ของคู่มัน ส่วน i คือ index ของ value ซึ่งเราเจอแล้วเพราะใช้สูตร pair = target - v)
# เลยเขียนแค่ i ได้เพราต้องการค่า index ของ value ที่ทำร่วมกับ pair ซึ่งคือ i ในรอบนั้น
# O(n)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = {}
        for i, v in enumerate(nums):
            pair = target - v
            if pair in nums_dict: return [nums_dict[pair], i]
            nums_dict[v] = i

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 2, 4], 6))
    print(solution.twoSum([3, 3], 6))