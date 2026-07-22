class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_min_index(nums):
            lo = 0
            hi = len(nums) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < nums[hi]:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        def binary_search(nums, target, lo, hi):
            while lo <= hi:
                mid = (lo + hi) // 2
                if target < nums[mid]:
                    hi = mid - 1
                elif target > nums[mid]:
                    lo = mid + 1
                else:
                    return mid
            return -1
        
        min_index = find_min_index(nums)
        left_arr = binary_search(nums, target, 0, min_index-1)
        right_arr = binary_search(nums, target, min_index, len(nums)-1)

        if left_arr != -1:
            return left_arr
        else:
            return right_arr