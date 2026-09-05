class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}

        for index, val in enumerate(nums):
            diff = target - val
            if diff in freq:
                return [freq[diff], index]
            freq[val] = index
        
        return None