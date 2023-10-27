class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = []

        for ch in s:
            val = ord(ch)

            if 97 <= val <= 122 or 48 <= val <= 57:
                ns.append(ch)
            elif 65 <= val <= 90:
                ns.append(chr(val + 32))

        return all(ns[i] == ns[~i] for i in range(len(ns) // 2))
