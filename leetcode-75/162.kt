class Solution {
    fun findPeakElement(nums: IntArray): Int {
        
        var left = 0
        var right = nums.size - 1

        while(left < right) {

            var mid = (left+right) / 2

            if(nums[mid] > nums[mid+1]) {
                right = mid
            } else {
                left = mid + 1
            }
        }
            return left
    }
}