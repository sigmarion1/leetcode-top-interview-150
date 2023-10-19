class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        characters = {}

        for ch in s:
            if ch not in characters:
                characters[ch] = 1
            else:
                characters[ch] += 1

        for ch in t:
            if ch not in characters:
                return False
            if characters[ch] == 1:
                characters.pop(ch)
            else:
                characters[ch] -= 1

        return True
