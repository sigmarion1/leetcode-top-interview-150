class Solution:
    def longestPalindrome(self, s: str) -> str:
        lth = len(s)

        dp = [[False] * lth for _ in range(lth)]

        for i in range(lth):
            dp[i][i] = True

        ans = s[0]

        for j in range(lth):
            for i in range(j):
                if s[i] == s[j] and (dp[i + 1][j - 1] or j == i + 1):
                    dp[i][j] = True
                    if j - i + 1 > len(ans):
                        ans = s[i : j + 1]

        return ans
