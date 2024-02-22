class Solution {
    fun uniqueOccurrences(arr: IntArray): Boolean {

        var hash = HashMap<Int, Int>()

        for(i in arr.indices) {
            var cur = arr[i]
            var curVal = hash.get(cur) ?: 0
            hash.put(cur, curVal + 1)
        }

        return hash.values.size == hash.values.distinct().size
    }
}