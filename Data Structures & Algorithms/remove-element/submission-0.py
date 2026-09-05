class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0

        for i in range(len(nums)):
            if nums[i]!=val:
                nums[left], nums[i] = nums[i], nums[left]
                left+=1
        return left