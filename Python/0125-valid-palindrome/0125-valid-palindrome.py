class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Psuedocode
        # take left =0 right = len(s)
        # string = s.toLowerCase()
        # take  a loop where we will check the ch  from left and right 
        # if a ch is not a number or a ch we will left ++ or right -- depends which side is not a ch if both are not ch we will move both 
        # if both are ch or num we will check 
        # if string[left]==string[right] return false 
        # if each ch are qeual return true

        left =0
        right =len(s)-1
        string=s.lower()

        while left < right:

            while not string[left].isalnum() and left<right: 
                left+=1
            while not string[right].isalnum() and right >left: 
                right-=1
            
            if string[right]!=string[left]:
                return False
            
            left+=1
            right-=1

        return True 
            

