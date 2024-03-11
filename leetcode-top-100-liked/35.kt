class Solution {
    fun searchInsert(nums: IntArray, target: Int): Int {
        var left = 0
        var right = nums.lastIndex

        while(left <= right) {

            var cur = (left + right) / 2

            if(nums[cur] == target) {
                return cur
            }

            if(nums[cur] < target) {
                left = cur + 1
            } else {
                right = cur - 1
            }
        }

        return left
    }
}