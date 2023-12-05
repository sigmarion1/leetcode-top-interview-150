class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        numch = ""
        cur = ""

        for ch in s:
            if ch.isdigit():
                numch += ch
            elif ch == "[":
                num = int(numch)
                numch = ""
                stack.append((num, cur))
                cur = ""
            elif ch == "]":
                cur_num, prv_cur = stack.pop()

                cur = prv_cur + cur * cur_num
            else:
                cur += ch

        return cur
