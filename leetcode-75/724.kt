class Solution {
    fun pivotIndex(nums: IntArray): Int {
        var sumLeft = 0
        var sumRight = nums.sum()

        for(i in nums.indices) {

            sumRight -= nums[i]

            if(sumRight == sumLeft) {
                return i
            }

            sumLeft += nums[i]
        }

        return -1
    }
}