class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        digits = {}

        for index, val in enumerate(nums):
            diff = target - val

            if diff in digits:
                return [digits[diff], index]
            
            digits[val] = index
        
        return -1