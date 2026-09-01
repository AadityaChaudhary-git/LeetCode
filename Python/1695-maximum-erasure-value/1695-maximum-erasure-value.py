class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        freq={}
        total=0
        ans=0
        left=0

        for right in range (n):
            freq[nums[right]]= freq.get(nums[right],0)+1
            total+=nums[right]
            
            while freq[nums[right]]>1:
                freq[nums[left]]-=1
                total-=nums[left]
                left+=1
            
            ans= max(total, ans)
    
        return ans


            
        
