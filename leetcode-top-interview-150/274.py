class Solution:
    def hIndex(self, citations: List[int]) -> int:
        lth = len(citations)

        citations.sort(reverse=True)

        for i in range(lth):
            if i + 1 == citations[i]:
                return i + 1
            elif i + 1 > citations[i]:
                return min(citations[i - 1], i)

        return lth
