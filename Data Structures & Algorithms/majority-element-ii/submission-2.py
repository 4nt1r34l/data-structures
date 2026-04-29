class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)

        return [x for x in freq if freq[x] > len(nums)/3]