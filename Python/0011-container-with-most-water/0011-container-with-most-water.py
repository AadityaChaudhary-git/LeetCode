class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        maximum_water =0
        left =0
        right =len(height)-1

        while left < right :
            current = min(height[left],height[right]) * (right-left)
            if current > maximum_water :
                maximum_water =current 
            
            if height [left]>height[right]:
                right-=1
            else : 
                left+=1
        
        return maximum_water


        