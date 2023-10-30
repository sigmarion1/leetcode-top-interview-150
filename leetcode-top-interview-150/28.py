class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = []
        for i in range(len(haystack)):
            n.append(i)
            new_n = []

            for start in n:
                if haystack[i] == needle[i - start]:
                    if i - start + 1 == len(needle):
                        return start
                    new_n.append(start)

            n = new_n

        return -1
