class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, len(s)-1
        window = set()
        maxSize = 0

        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left+=1
            
            window.add(s[right])

            maxSize = max(maxSize, right-left+1)
        
        return maxSize
