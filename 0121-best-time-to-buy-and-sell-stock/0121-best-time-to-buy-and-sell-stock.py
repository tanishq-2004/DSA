class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r =  1
        max_profit = 0

        for r in range(len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit , profit)
            elif prices[r] < prices[l]:
                l = r
            else:
                r += 1
        return max_profit
