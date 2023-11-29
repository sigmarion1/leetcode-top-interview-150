class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        dI = None
        maxLen = 0

        for i, num in enumerate(nums):
            if not num:
                if dI is None:
                    dI = i
                else:
                    left = dI + 1
                    dI = i

            maxLen = max(maxLen, i - left)

        return maxLen
