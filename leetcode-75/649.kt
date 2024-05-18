class Solution {
    fun predictPartyVictory(senate: String): String {

        var vanR = 0
        var vanD = 0
        var senateList: MutableList<Char> = senate.toMutableList()
        var countR = senateList.count { it == 'R' }
        var countD = senateList.count { it == 'D' }

        while(true) {
            if(senateList.count { it == 'R' } == 0) {
                return "Dire"
            }
            if(senateList.count { it == 'D' } == 0) {
                return "Radiant"
            }

            vanR = 0
            vanD = 0

            for(i in senateList.indices) {
                if(senateList[i] == 'R') {
                    if(vanR > 0) {
                        vanR--
                        senateList[i] = '-'
                    } else {
                        vanD++
                    }
                } else if(senateList[i] =='D') {
                    if(vanD > 0) {
                        vanD--
                        senateList[i] = '-'
                    } else {
                        vanR++
                    }
                } 
            }

            for(i in senateList.indices) {
                if(vanR == 0 && vanD == 0) {
                    break
                }
                if(senateList[i] == 'R') {
                    if(vanR > 0) {
                        vanR--
                        senateList[i] = '-'
                    }
                } else if(senateList[i] =='D') {
                    if(vanD > 0) {
                        vanD--
                        senateList[i] = '-'
                    } 
                } 
            }

        }

    }
}
