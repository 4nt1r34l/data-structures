class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        right = m + n - 1
        mEnd = m-1
        nEnd = n-1

        while nEnd >= 0:
            if mEnd >= 0 and nums1[mEnd] > nums2[nEnd]:
                nums1[right] = nums1[mEnd]
                mEnd-=1
            else:
                nums1[right] = nums2[nEnd]
                nEnd-=1
            right-=1
        