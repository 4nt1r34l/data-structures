class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for index, val in enumerate(nums):
            diff = target - val
            if diff in d:
                return [d[diff], index]
            d[val] = index
        
        return None