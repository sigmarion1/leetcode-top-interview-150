class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)

        result = [""] * (n1 + n2)

        i = 0
        j = 0

        while i + j < n1 + n2:
            if i < n1:
                result[i + j] = word1[i]
                i += 1
            if j < n2:
                result[i + j] = word2[j]
                j += 1

        return "".join(result)
