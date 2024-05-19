class Solution {
    fun compress(chars: CharArray): Int {

        var cur = chars[0]
        var count = 1
        var oIndex = 0

        for(i in 1 until chars.size) {
            if(cur == chars[i]) {
                count++
            } else {
                chars[oIndex] = cur
                oIndex++

                if(count > 1) {
                    val countChars = count.toString().toCharArray()
                    for(chr in countChars) {
                        chars[oIndex] = chr
                        oIndex++
                    }
                }

                cur = chars[i]
                count = 1
            }
        }

        chars[oIndex] = cur
        oIndex++

        if(count > 1) {
            val countChars = count.toString().toCharArray()
            for(chr in countChars) {
                chars[oIndex]=chr
                oIndex++
            }
        }

        return oIndex

    }
}