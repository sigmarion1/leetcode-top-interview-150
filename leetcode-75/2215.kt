class Solution {
    fun findDifference(nums1: IntArray, nums2: IntArray): List<List<Int>> {
        var set1 = nums1.toSet()
        var set2 = nums2.toSet()

        return(listOf(set1.subtract(set2).toList(), set2.subtract(set1).toList()))
    
    }
}