class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        R = 0
        max_window = 0
        count = 0

        while R < len(nums):
            if nums[R] == 1:
                count+=1
                max_window = max(max_window, count)
            else:
                count = 0
            R+=1
        return max_window