class Solution {
    fun numIslands(grid: Array<CharArray>): Int {
        val visited = mutableSetOf<Pair<Int, Int>>()
        var count = 0

        val m = grid.lastIndex
        val n = grid[0].lastIndex

        val dir = arrayOf(Pair(1,0), Pair(-1,0), Pair(0,1), Pair(0,-1))

        for(i in grid.indices) {
            for(j in grid[0].indices) {
                
                if(Pair(j, i) in visited) {
                    continue
                }

                if(grid[i][j] == '1') {

                    count += 1

                    val dq = ArrayDeque<Pair<Int, Int>>()
                    dq.addFirst(Pair(j, i))

                    while(dq.isNotEmpty()) {
                        var cur = dq.removeLast()

                        if(cur in visited) {
                            continue
                        }

                        var (x, y) = cur

                        if(grid[y][x] == '1') {

                            for(dirPair in dir) {
                                var new_x = x + dirPair.first
                                var new_y = y + dirPair.second

                                if(new_x >= 0 && new_x <= n && new_y >= 0 && new_y <= m) {
                                    if(grid[new_y][new_x] == '1') {
                                        dq.addFirst(Pair(new_x, new_y))
                                    }
                                }
                            }

                        }

                        visited.add(cur)
                    }


                        


                    }  
                    visited.add(Pair(j, i))  
                
                }

     
                

            }


        return count
    }
}