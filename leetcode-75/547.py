class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        checked = set()
        count = 0

        def dfs(cur):
            for i in range(n):
                if i == cur or i in checked:
                    continue

                if isConnected[cur][i]:
                    checked.add(i)
                    dfs(i)

        for i in range(n):
            if i not in checked:
                count += 1
                dfs(i)

        return count
