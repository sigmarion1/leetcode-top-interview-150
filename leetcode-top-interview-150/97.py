class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False

        memo = {}

        def helper(i: int, j: int, k: int) -> bool:
            if k == l:
                return True
            
            if (i, j) in memo:
                return memo[(i, j)]

            ans = False
            if i < m and s1[i] == s3[k]:
                ans = ans or helper(i + 1, j, k + 1)

            if j < n and s2[j] == s3[k]:
                ans = ans or helper(i, j + 1, k + 1)

            memo[(i, j)] = ans
            return ans

        return helper(0, 0, 0)

        if not s1 and not s2 and not s3:
            return True

        if not s3:
            return False

        s1_inter, s2_inter = False, False

        if s1 and s1[0] == s3[0]:
            s1_inter = self.isInterleave(s1[1:], s2, s3[1:])
            
        if s2 and s2[0] == s3[0]:
            s2_inter = self.isInterleave(s1, s2[1:], s3[1:])

        return s1_inter or s2_inter
        