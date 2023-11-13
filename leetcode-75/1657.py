class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        def countCharacter(word):
            counts = []

            for ch in set(word):
                counts.append(word.count(ch))

            return sorted(counts)

        return countCharacter(word1) == countCharacter(word2)
