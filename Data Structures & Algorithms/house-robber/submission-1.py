class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def _rob(nums, i, memo):
            if i in memo:
                return memo[i]
            
            if i >= len(nums):
                return 0
            
            take = nums[i] + _rob(nums, i+2, memo)
            not_take = _rob(nums, i+1, memo)
            memo[i] = max(take, not_take) 
            return memo[i]

        return _rob(nums, 0, {})
    