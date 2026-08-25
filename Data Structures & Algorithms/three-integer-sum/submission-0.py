class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        total = set()
        nums.sort()

        for start in range(len(nums)-1):
            left, right = start + 1, len(nums)-1

            if nums[start]>0:
                break
            
            if start > 0 and nums[start] == nums[start-1]:
                continue

            while left<right:
                totalSum = nums[start] + nums[left] + nums[right]

                if not totalSum:
                    total.add((nums[start],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif totalSum > 0:
                    right-=1
                else:
                    left+=1

        return list(total)