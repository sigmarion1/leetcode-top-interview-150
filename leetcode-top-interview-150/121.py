class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pf = 0
        min_p = prices[0]
        max_p = prices[0]

        for i in range(len(prices)):
            if prices[i] < min_p:
                min_p = prices[i]
                max_p = prices[i]
            elif prices[i] > max_p:
                max_p = prices[i]
                pf = max(pf, max_p - min_p)

        return pf
