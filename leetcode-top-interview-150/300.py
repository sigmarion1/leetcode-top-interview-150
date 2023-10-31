class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lth = len(nums)
        dp = [1] * lth

        for i in range(1, lth):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
