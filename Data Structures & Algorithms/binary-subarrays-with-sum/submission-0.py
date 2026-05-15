class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq = {0: 1}
        count, curSum = 0, 0

        for right in range(len(nums)):
            curSum += nums[right]
            count += freq.get(curSum - goal, 0)
            freq[curSum] = 1 + freq.get(curSum, 0)
        return count