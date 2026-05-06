class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                cost += (prices[i] - prices[i-1])
        
        return cost
