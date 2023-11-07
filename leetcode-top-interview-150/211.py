class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        cur = self.trie

        for ch in word:
            if ch not in cur:
                cur[ch] = dict()
            cur = cur[ch]

        cur["end"] = True

    def recursiveSearch(self, word, trie):
        if type(trie) is not dict:
            return False

        if not word:
            if "end" in trie:
                return True
            else:
                return False

        if word[0] == ".":
            for v in trie.values():
                if self.recursiveSearch(word[1:], v):
                    return True
        elif word[0] in trie:
            return self.recursiveSearch(word[1:], trie[word[0]])

        return False

    def search(self, word: str) -> bool:
        return self.recursiveSearch(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
