class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq={}
        freq2={}

        if len(s)==len(t):

            for ch in s:
                freq[ch]= freq.get(ch,0)+1

            for ch in t:
                freq2[ch]=freq2.get(ch,0)+1

            if freq ==freq2:
                return True 
            else :
                return False 
        
        else : 
            return False 
            
        