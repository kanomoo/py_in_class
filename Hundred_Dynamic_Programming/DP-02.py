# class Solution:
#     # O(n log n)
#     def sortedSquares(self, nums: list[int]) -> list[int]:
#         return sorted(i ** 2 for i in nums)

# if __name__ == "__main__":
#     sorted_squares = Solution()
#     print(sorted_squares.sortedSquares([0, 2, -10, 10, 5]))


# ต้อง sorted มาก่อน input  O(n)
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # 2 Pointers    Biggest squares are on the ends
        n = len(nums)
        res = [0] * n
        L, R = 0, n - 1

        for i in range(n - 1, -1, -1):
            if abs(nums[L]) > abs(nums[R]):
                val = nums[L]
                L += 1
            else:
                val = nums[R]
                R -= 1
            
            res[i] = val ** 2
    
        return res


if __name__ == "__main__":
    sorted_squares = Solution()
    print(sorted_squares.sortedSquares([0, 2, -10, 10, 0]))