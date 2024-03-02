class Solution {
    fun letterCombinations(digits: String): List<String> {
        
        val digitMap = mapOf('2' to arrayOf('a','b','c'), '3' to arrayOf('d','e','f'), '4' to arrayOf('g','h','i'), '5' to arrayOf('j','k','l'), '6' to arrayOf('m','n','o'), '7' to arrayOf('p','q','r','s'), '8' to arrayOf('t','u','v'), '9' to arrayOf('w','x','y','z'))

        var queue = ArrayDeque<Pair<String, String>>()

        var result = ArrayList<String>()

        queue.add(digits to "")

        while(queue.size > 0) {

            val currentPair = queue.removeFirst()
            val currentDigits = currentPair.first
            val currentStr = currentPair.second

            if (currentDigits.length == 0) {
                if(currentStr.length > 0) {
                    result.add(currentStr)
                }
                continue
            }

            val key = currentDigits[0]

            digitMap[key]?.let { chars ->
            for (char in chars) {
                queue.add(currentDigits.substring(1) to currentStr+char)
                }
            }
        
        }

        return result

    }
}