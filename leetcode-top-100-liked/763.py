class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        last = dict()

        for i in range(n):
            last[s[i]] = i

        result = [last[s[0]]]

        for i in range(1, n):
            if i > result[-1]:
                result.append(last[s[i]])
            else:
                result[-1] = max(result[-1], last[s[i]])

        for i in range(len(result) - 1, 0, -1):
            result[i] = result[i] - result[i - 1]

        result[0] = result[0] + 1

        return result
