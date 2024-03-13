class Solution {
    fun maxProfit(prices: IntArray): Int {
    
        var maxVal = 0
        var buyVal = prices[0]

        for(i in 1..prices.lastIndex) {
            var curVal = prices[i]

            if(curVal < buyVal) {
                buyVal = curVal
            } else {
                maxVal = max(maxVal, curVal - buyVal)
            }
        }
        return maxVal
    }
}