class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        left = 0
        right = n - 1
        result = [0] * n
        i = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2   # blank 1
                left += 1
            else:
                result[i] = nums[right] ** 2  # blank 2
                right -= 1
            i -=1                             # blank 3

        return result