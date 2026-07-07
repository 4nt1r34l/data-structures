class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for start in range(len(nums)-2):
            left = start + 1
            right = len(nums)-1

            if nums[start] > 0:
                break

            if start > 0 and nums[start] == nums[start-1]:
                continue

            while left<right:
                total = nums[start] + nums[left] + nums[right]

                if not total:
                    res.append([nums[start], nums[left], nums[right]])
                    left+=1
                    while nums[left] == nums[left-1] and left<right:
                        left+=1
                elif total>0:
                    right-=1
                else:
                    left+=1
        
        return res