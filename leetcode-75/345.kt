class Solution {
    fun reverseVowels(s: String): String {
        
        val vowels: Array<Char> = arrayOf('a', 'e', 'i', 'o', 'u', 'A','E', 'I', 'O', 'U')
        var sb = StringBuilder()
        var stack = Stack<Char>()

        for (ch in s) {
            sb.append(ch)
            if (ch in vowels) {
                stack.push(ch)
            }
        }

        for (i in sb.indices) {
            if (sb[i] in vowels) {
                sb[i] = stack.pop()
            }
        }

        return sb.toString()
    }
}