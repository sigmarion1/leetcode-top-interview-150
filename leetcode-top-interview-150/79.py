class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        vects = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        history = set()
        isFound = False

        def findWord(coordi, lword, history):
            nonlocal isFound

            if isFound or coordi in history:
                return

            x, y = coordi[0], coordi[1]

            if board[y][x] == lword[0]:
                history.add((x, y))

                if not lword[1:]:
                    isFound = True
                    return

                for vect in vects:
                    nx = x + vect[0]
                    ny = y + vect[1]

                    if 0 <= nx < n and 0 <= ny < m:
                        findWord((nx, ny), lword[1:], history)

                history.remove((x, y))

        for i in range(m):
            for j in range(n):
                findWord((j, i), word, set())

        return isFound
