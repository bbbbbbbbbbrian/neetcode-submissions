class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minimum = prices[0]
        for i in range(len(prices)):
            if max_profit < prices[i] - minimum:
                max_profit = prices[i] - minimum
            if prices[i] < minimum:
                minimum = prices[i]
        return max_profit

