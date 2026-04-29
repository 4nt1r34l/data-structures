class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        freq = {}

        for index, val in enumerate(numbers):
            diff = target - val

            if diff in freq:
                return [freq[diff]+1, index+1]
            
            freq[val] = index
        
        return -1