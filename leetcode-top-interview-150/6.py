class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]

        cycle = numRows + (numRows - 2)

        for i in range(len(s)):
            cur = i % cycle
            print(cur)

            if cur < numRows:
                rows[cur].append(s[i])
            else:
                rows[cycle - cur].append(s[i])

        results = ""

        for ch_list in rows:
            results += "".join(ch_list)

        return results
