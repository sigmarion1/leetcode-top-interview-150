class Solution:
    def numTilings(self, n: int) -> int:
        dp1, dp2 = [1, 2] + [0] * (n - 2), [1] * n

        for i in range(2, n):
            dp1[i] = dp1[i - 1] + dp1[i - 2] + dp2[i - 1] * 2
            dp2[i] = dp1[i - 2] + dp2[i - 1]

        return dp1[n - 1] % 1000000007
