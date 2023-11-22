class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)

        prv = 0
        cnt = 1

        for i in range(1, n):
            if intervals[i][0] >= intervals[prv][1]:
                prv = i
                cnt += 1

        return n - cnt
