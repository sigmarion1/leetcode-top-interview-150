class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ori = defaultdict(set)
        rev = defaultdict(set)

        count = 0

        for connect in connections:
            start, end = connect
            ori[start].add(end)
            rev[end].add(start)

        stack = [0]
        history = set()

        while stack:
            cur = stack.pop()
            history.add(cur)

            for nxt in ori[cur]:
                if nxt not in history:
                    count += 1
                    rev[cur].add(nxt)

            for nxt in rev[cur]:
                if nxt not in history:
                    stack.append(nxt)

        return count
