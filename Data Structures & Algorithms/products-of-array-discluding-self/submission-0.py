class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        curProd = 1

        for n in nums:
            prefix.append(curProd)
            curProd *= n
        
        curProd = 1
        for n in range(len(nums)-1, -1, -1):
            prefix[n] *= curProd
            curProd *= nums[n]
        
        return prefix