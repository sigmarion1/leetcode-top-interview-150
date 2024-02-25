class Solution {
    fun tribonacci(n: Int): Int {

        var triboList = arrayListOf(0, 1, 1)

        while(triboList.size < n+1) {
            var i = triboList.lastIndex
            triboList.add(triboList[i] + triboList[i-1] + triboList[i-2])
        }

        return triboList[n]
    }
}