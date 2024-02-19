class Solution {
    fun moveZeroes(nums: IntArray): Unit {
        var cur = 0

        for(i in nums.indices) {
            if(nums[i] == 0) {
                continue
            }

            if(i > cur) {
                nums[cur] = nums[i]
            }

            cur += 1
        }

        for(i in cur until nums.size) {
            nums[i] = 0
        }
    }
}