class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def _coinChange(coins, amount, memo):
            if amount < 0:
                return float('inf')

            if amount == 0:
                return 0
            
            if amount in memo:
                return memo[amount]
            
            minCoin = float("inf")
            for c in coins:
                coin = 1 + _coinChange(coins, amount-c, memo)
                minCoin = min(coin, minCoin)
                memo[amount] = minCoin

            return memo[amount]
        
        coin = _coinChange(coins, amount, {})

        if coin != float('inf'):
            return coin
        
        return -1