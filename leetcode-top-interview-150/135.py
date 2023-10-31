class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        cds = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                cds[i] = cds[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                cds[i] = max(cds[i], cds[i + 1] + 1)

        return sum(cds)
