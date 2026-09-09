class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """

        left =0
        right=n
        arr=[]

        
        while left <n:
            arr.append(nums[left])
            arr.append(nums[right])
            left+=1
            right+=1

        return arr

        