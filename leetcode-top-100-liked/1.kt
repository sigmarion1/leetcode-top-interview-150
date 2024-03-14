class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val map: MutableMap<Int, Int> = mutableMapOf()

        for(i in nums.indices) {
            var curVal = nums[i]
            if(map.contains(target - curVal)){
                return intArrayOf(i, map[target-curVal]!!)
            }

            map[curVal] = i
        }

        return intArrayOf(1,1)

    }
}