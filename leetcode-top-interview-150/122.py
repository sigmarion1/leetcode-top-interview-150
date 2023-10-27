class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_hold, cur_not_hold = -float("inf"), 0

        for price in prices:
            prv_hold, prv_not_hold = cur_hold, cur_not_hold

            cur_hold = max(prv_hold, prv_not_hold - price)
            cur_not_hold = max(prv_not_hold, prv_hold + price)

        return cur_not_hold
