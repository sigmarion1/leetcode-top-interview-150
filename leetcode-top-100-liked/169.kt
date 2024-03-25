class Solution {
    fun majorityElement(nums: IntArray): Int {
        var major = nums[0]
        var count = 0

        for(num in nums) {
            if(count == 0) {
                major = num
                count = 1
            } else if(major == num) {
                count += 1
            } else {
                count -= 1
            }
        }
        return major
    }
}