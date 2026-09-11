class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1 1 2 
        l =0
        for r in range(1,len(nums)):

            #nums[R]==nums[L] → R moves forward (skip)
            #nums[R]!=nums[L] → L moves, copy R to L
            if nums[l]!=nums[r]: 
                l+=1
                nums[l]=nums[r]
           
        return l+1 
        #remaining elements beyond index k - 1 can be ignored.