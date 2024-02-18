class Solution {
    fun canPlaceFlowers(flowerbed: IntArray, n: Int): Boolean {
        
        if(n==0) {
            return true
        }

        var curN = n
        val lastIndex = flowerbed.size - 1

        for(i in flowerbed.indices) {
            if(flowerbed[i]==1) {
                continue
            }
            
            if(i!=0 && flowerbed[i-1]==1) {
                continue
            }

            if(i!=lastIndex && flowerbed[i+1]==1) {
                continue
            }

            flowerbed[i] = 1
            curN -= 1

            if(curN==0) {
                return true
            }
        }

        return false

    }
}