class Solution {
    fun reverseWords(s: String): String {
        
        var result: ArrayList<String> = ArrayList()
        var word: ArrayList<Char> = ArrayList()

        for (char in s) {
            if (char == ' ') {
                if (word.size > 0) {
                    result.add(word.joinToString(separator = ""))
                    word.clear()
                }
                continue
            } 
            word.add(char)
        }

        if (word.size > 0) {
            result.add(word.joinToString(separator = ""))
            word.clear()
        }

        return result.reversed().joinToString(separator = " ")
    }
}