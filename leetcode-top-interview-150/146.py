class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prv = None
        self.nxt = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.oldest = Node(0, 0)
        self.latest = Node(0, 0)
        self.oldest.nxt = self.latest
        self.latest.prv = self.oldest

    def remove(self, node):
        prv, nxt = node.prv, node.nxt
        prv.nxt = nxt
        nxt.prv = prv

    def insert(self, node):
        prv, nxt = self.latest.prv, self.latest
        prv.nxt = nxt.prv = node
        node.nxt = nxt
        node.prv = prv

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.oldest.nxt
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
