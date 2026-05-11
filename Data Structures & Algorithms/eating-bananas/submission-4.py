class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        minTime = right

        while left<=right:
            mid = (left+right)//2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile)/mid)
            
            if totalTime <= h:
                minTime = min(mid, minTime)
                right = mid-1
            else:
                left = mid+1
        return minTime