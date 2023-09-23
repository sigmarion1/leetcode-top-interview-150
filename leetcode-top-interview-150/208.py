class Trie:
    def __init__(self):
        self.first = {}

    def insert(self, word: str) -> None:
        cur = self.first

        for ch in word:
            if ch in cur:
                cur = cur[ch]
            else:
                cur[ch] = {}
                cur = cur[ch]

        cur["isEnd"] = True

    def search(self, word: str) -> bool:
        cur = self.first

        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]

        if "isEnd" not in cur:
            return False

        return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.first

        for ch in prefix:
            if ch not in cur:
                return False
            cur = cur[ch]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
