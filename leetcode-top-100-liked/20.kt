class Solution {
    fun isValid(s: String): Boolean {
        var stack = Stack<Char>()

        var map = mapOf('(' to ')', '{' to '}', '[' to ']')

        for (char in s) {
            if(char in map.keys) {
                stack.push(char)
                continue
            }

            if(stack.size == 0) {
                return false
            }

            if(char != map[stack.pop()]) {
                return false
            }
        }
        
        if(stack.size == 0){
            return true
        }

        return false    

    }
}