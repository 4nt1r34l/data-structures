class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = 0

        while True:
            if n not in nums:
                return n
            n+=1
        