class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        results = []
        current_max = float("-inf")

        for interval in intervals:
            if current_max < interval[0]:
                results.append(interval)
                current_max = interval[1]
            elif current_max >= interval[0]:
                current_max = max(current_max, interval[1])
                results[-1][1] = current_max

        return results
