class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        values = set(nums)

        for n in values:
            if (n-1) not in values:
                length = 1
                while (n+length) in values:
                    length+=1
                ans = max(ans, length)

        return ans 