class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        res = 0

        while left <= right:
            mid = (left+right)//2
            exp = mid**2

            if exp == x:
                return mid
            elif exp < x:
                left = mid + 1
            else:
                right = mid-1
        return right