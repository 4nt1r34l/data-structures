class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left<right:
            if s[left] != s[right]:
                start = s[left+1:right+1] == s[left+1:right+1][::-1]
                end = s[left:right] == s[left:right][::-1]
                return (start or end)
            left+=1
            right-=1
        
        return True