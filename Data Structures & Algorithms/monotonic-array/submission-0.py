class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True

        stack = []
        if nums[0] > nums[1]:
            for i in range(len(nums)):
                while stack and stack[-1] < nums[i]:
                    return False
                stack.append(nums[i])
            
        else:
            for i in range(len(nums)):
                while stack and stack[-1] > nums[i]:
                    return False
                stack.append(nums[i])
        
        return True