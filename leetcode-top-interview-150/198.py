class Solution:
    def rob(self, nums: List[int]) -> int:
        lth = len(nums)

        if lth <= 2:
            return max(nums)

        dp = [0] * lth

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, lth):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]
