"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        n = len(grid)

        val = None
        isLeaf = True

        for i in range(n):
            row = grid[i]

            if isLeaf:
                if row.count(row[0]) == n:
                    if val is None:
                        val = row[0]
                    elif val != row[0]:
                        isLeaf = False
                else:
                    isLeaf = False

        if isLeaf:
            return Node(val, isLeaf, None, None, None, None)

        else:
            tl, tr, bl, br = [], [], [], []
            for i in range(n):
                l, r = [], []
                for j in range(n):
                    if j < n / 2:
                        l.append(grid[i][j])
                    else:
                        r.append(grid[i][j])

                if i < n / 2:
                    tl.append(l)
                    tr.append(r)

                else:
                    bl.append(l)
                    br.append(r)

            topLeft = self.construct(tl)
            topRight = self.construct(tr)
            bottomLeft = self.construct(bl)
            bottomRight = self.construct(br)

            return Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight)
