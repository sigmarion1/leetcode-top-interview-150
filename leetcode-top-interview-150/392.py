class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0

        for i in range(len(t)):
            if si == len(s):
                return True

            if s[si] == t[i]:
                si += 1

        return si == len(s)
