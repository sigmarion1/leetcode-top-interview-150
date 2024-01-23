from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        pDict = defaultdict(int)

        for ch in p:
            pDict[ch] += 1

        curDict = defaultdict(int)

        for i in range(len(p) - 1):
            curDict[s[i]] += 1

        result = []

        for i in range(len(s) - len(p) + 1):
            curDict[s[i + len(p) - 1]] += 1
            if pDict == curDict:
                result.append(i)
            curDict[s[i]] -= 1
            if curDict[s[i]] == 0:
                del curDict[s[i]]

        return result
