class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])

        edge = set()

        for x in range(n):
            edge.add((x, 0))
            edge.add((x, m - 1))

        for y in range(m):
            edge.add((0, y))
            edge.add((n - 1, y))

        surrounded_o = set()
        not_surrounded = set()

        def check_surrounded(x, y, block):
            if board[y][x] == "X":
                return True

            if (x, y) in block:
                return True

            if (x, y) in edge:
                return False

            block.add((x, y))

            up = check_surrounded(x, y - 1, block)
            down = check_surrounded(x, y + 1, block)
            right = check_surrounded(x + 1, y, block)
            left = check_surrounded(x - 1, y, block)

            return all((up, down, right, left))

        for x in range(n):
            for y in range(m):
                if (x, y) in not_surrounded or (x, y) in surrounded_o:
                    continue
                if board[y][x] == "O":
                    block = set()
                    if check_surrounded(x, y, block):
                        surrounded_o.update(block)
                    else:
                        not_surrounded.update(block)

        for x, y in surrounded_o:
            board[y][x] = "X"
