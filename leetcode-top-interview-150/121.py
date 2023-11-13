class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pf = 0
        minP = prices[0]

        for price in prices:
            if price < minP:
                minP = price
            else:
                pf = max(pf, price - minP)

        return pf
