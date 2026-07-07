class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left<right:
            if s[left] != s[right]:
                left_delete = s[left+1:right+1]
                right_delete = s[left:right]
                return left_delete == left_delete[::-1] or right_delete == right_delete[::-1]
            left+=1
            right-=1
        return True