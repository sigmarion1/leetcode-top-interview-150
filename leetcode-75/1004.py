class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLen = 0

        start = 0
        curFlip = 0

        for i in range(len(nums)):
            if not nums[i]:
                curFlip += 1

            while curFlip > k:
                if not nums[start]:
                    curFlip -= 1
                start += 1

            maxLen = max(maxLen, i - start + 1)

        return maxLen
