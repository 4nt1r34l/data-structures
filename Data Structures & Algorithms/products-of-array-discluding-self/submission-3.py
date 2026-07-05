class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = deque([])
        suffix = deque([])

        total = 1
        for i in range(len(nums)):
            prefix.append(total)
            total*=nums[i]
        
        total = 1
        for i in range(len(nums)-1, -1, -1):
            suffix.appendleft(total)
            total*=nums[i]
        
        res = []
        for i in range(len(nums)):
            res.append(prefix[i]*suffix[i])
            
        return res