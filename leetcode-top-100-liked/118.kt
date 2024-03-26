class Solution {
    fun generate(numRows: Int): List<List<Int>> {
        var result = mutableListOf<List<Int>>()

        for(i in 1..numRows) {
            var rows = MutableList(i){1}

            for(j in 1..i-2) {
                rows[j] = result[i - 2][j] + result[i - 2][j - 1]
            }

            result.add(rows)
        }

        return result
    }
}