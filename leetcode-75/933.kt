class RecentCounter() {

    var ar: ArrayList<Int> = arrayListOf<Int>()
    var cur: Int = 0

    fun ping(t: Int): Int {

        while(cur < ar.size){
            if(ar[cur] >= t - 3000) {
                break
            }
            cur += 1
        }

        ar.add(t)

        return ar.size - cur
    }

}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = RecentCounter()
 * var param_1 = obj.ping(t)
 */