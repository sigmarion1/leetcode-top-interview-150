class Solution {
    fun climbStairs(n: Int): Int {
        var dp = IntArray(n) { 0 }

        dp[0] = 1

        if(n>1) {
            dp[1] = 2
        }

        for(i in 2..n-1) {
            dp[i] = dp[i-1] + dp[i-2]
        }

        return dp[dp.lastIndex]
    }
}