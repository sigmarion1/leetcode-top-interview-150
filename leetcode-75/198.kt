class Solution {
    fun rob(nums: IntArray): Int {
    
        if (nums.size <= 2) {
            return nums.maxOrNull() ?: 0
        }

        var dp = Array<Int>(nums.size){0}

        dp[0] = nums[0]
        dp[1] = Math.max(nums[0], nums[1])

        for(i in 2..nums.size-1) {
            dp[i] = maxOf(dp[i-2]+nums[i], dp[i-1])
        }

        return dp.last()
    }
}