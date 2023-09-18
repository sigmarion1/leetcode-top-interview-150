class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []

        for i in range(len(strs[0])):
            current = None

            try:
                for str in strs:
                    if not current:
                        current = str[i]
                    elif current != str[i]:
                        return "".join(result)

            except IndexError:
                return "".join(result)

            result.append(current)

        return "".join(result)
