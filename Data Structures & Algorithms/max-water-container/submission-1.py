class Solution:
    def maxArea(self, h: List[int]) -> int:
        left = 0
        right = len(h)-1
        res = 0

        while left < right:
            area = min(h[left], h[right]) * (right-left)
            res = max(res, area)

            if h[left]<h[right]:
                left+=1
            else:
                right-=1
        
        return res
