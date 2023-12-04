class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = Counter(map(tuple, grid))
        cols = Counter(zip(*grid))

        return sum(cols[row] * rows[row] for row in rows)
