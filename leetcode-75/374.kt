/** 
 * The API guess is defined in the parent class.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * fun guess(num:Int):Int {}
 */

class Solution:GuessGame() {
    override fun guessNumber(n:Int):Int {

        var l = 1
        var r = n

        while(l<=r) {
            var mid = l + (r-l)/ 2

            var result = guess(mid)

            if(result == 0) {
                return mid
            } else if (result == 1) {
                l = mid + 1
            } else {
                r = mid -1
            }
        }
        return l
    }
}

