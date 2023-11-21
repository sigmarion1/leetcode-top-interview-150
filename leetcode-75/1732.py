class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur = 0
        maxAlt = 0

        for val in gain:
            cur += val
            maxAlt = max(maxAlt, cur)

        return maxAlt
