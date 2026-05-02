class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def _coin(amount, coins, memo):

            if amount in memo:
                return memo[amount]

            if amount == 0:
                return 0
            
            if amount < 0:
                return float("inf")
            
            coin = float("inf")

            for c in coins:
                nums = 1 + _coin(amount-c, coins, memo)
                coin = min(coin, nums)
            memo[amount] = coin
            
            return coin
        
        ans = _coin(amount, coins, {})

        if ans == float("inf"):
            return -1
        
        return ans
