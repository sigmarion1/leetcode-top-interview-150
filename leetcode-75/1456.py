class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}

        start, end = 0, k - 1
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1

        maxCount = count

        for i in range(1, len(s) - k + 1):
            start = i
            end = i + k - 1

            if s[start - 1] in vowels:
                count -= 1
            if s[end] in vowels:
                count += 1

            maxCount = max(maxCount, count)

        return maxCount
