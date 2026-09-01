class Solution(object):
    def minWindow(self, s, t):
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        have = {}
        formed = 0
        required = len(need)
        ans = ""
        left = 0

        for right in range(len(s)):
            ch = s[right]
            have[ch] = have.get(ch, 0) + 1

            if ch in need and have[ch] == need[ch]:
                formed += 1

            while formed == required:
                if ans == "" or right - left + 1 < len(ans):
                    ans = s[left:right+1]
                have[s[left]] -= 1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1

        return ans