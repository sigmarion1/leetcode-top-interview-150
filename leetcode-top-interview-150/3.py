class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lth = len(s)

        subSet = dict()
        maxSubLen = 0
        startIdx = 0

        for i in range(lth):
            ch = s[i]

            if ch in subSet:
                maxSubLen = max(i - startIdx, maxSubLen)
                prvIdx = startIdx
                startIdx = subSet[ch] + 1

                for j in range(prvIdx, startIdx):
                    subSet.pop(s[j], None)

            subSet[ch] = i

        return max(lth - startIdx, maxSubLen)
