class Solution {
    fun findMaxAverage(nums: IntArray, k: Int): Double {
        
        var sum = 0

        for(i in 0..(k-1)) {
            sum += nums[i]
        }

        var maxSum = sum

        for(i in k..nums.size-1) {
            sum -= nums[i-k]
            sum += nums[i]

            maxSum = max(maxSum, sum)
        }

        return maxSum.toDouble() / k.toDouble()

    }
}