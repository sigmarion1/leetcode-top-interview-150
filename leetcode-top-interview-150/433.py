from collections import deque


class Solution:
    def isMutate(self, first, second):
        diffCnt = 0

        for i in range(8):
            if first[i] != second[i]:
                diffCnt += 1
        return diffCnt == 1

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque()
        visited = set()
        q.append((startGene, 0))

        while q:
            cur, cnt = q.popleft()

            if cur == endGene:
                return cnt

            for gene in bank:
                if self.isMutate(cur, gene) and gene not in visited:
                    q.append((gene, cnt + 1))
                    visited.add(gene)

        return -1
