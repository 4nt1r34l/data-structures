class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        left = 0
        curProd = 1

        if k == 0:
            return 0

        for right in range(len(nums)):
            curProd *= nums[right]
            while curProd >= k and left<=right:
                curProd //= nums[left]
                left+=1
            res += (right-left+1)
        
        return res