class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                val = prices[j]-prices[i]
                if val > maximum:
                    maximum = val
        if maximum < 0:
            return 0
        return maximum
                 
