class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = [0] * n
        right = [0] * n

        start, end = 1, 1

        for i in range(n):
            j = -i-1
            left[i] = start
            right[j] = end
            start*=nums[i]
            end*= nums[j]
        
        return [l*r for l,r in zip(left,right)]