class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        START, END = 0, 1

        [s, e] = newInterval

        left = []
        right = []

        for cur_interval in intervals:
            if cur_interval[END] < s:
                left.append(cur_interval)
            elif cur_interval[START] > e:
                right.append(cur_interval)
            else:
                s = min(s, cur_interval[START])
                e = max(e, cur_interval[END])

        return left + [[s, e]] + right
