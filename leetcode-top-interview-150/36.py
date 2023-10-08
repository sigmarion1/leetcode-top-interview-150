class Solution:
    def isValidNumbers(self, numbers: List[str]) -> bool:
        values = set()

        for number in numbers:
            if number == ".":
                continue
            elif number in values:
                return False
            else:
                values.add(number)

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [[] for _ in range(9)]
        subBox = [[] for _ in range(9)]
        vect = [
            (-1, -1),
            (-1, 0),
            (0, -1),
            (0, 0),
            (1, 0),
            (0, 1),
            (1, 1),
            (-1, 1),
            (1, -1),
        ]
        Center = 4

        for i in range(9):
            if not self.isValidNumbers(board[i]):
                return False

            subBoxCenter = (4 + vect[i][0] * 3, 4 + vect[i][1] * 3)

            for j in range(9):
                cols[i].append(board[j][i])

                x = subBoxCenter[0] + vect[j][0]
                y = subBoxCenter[1] + vect[j][1]

                subBox[i].append(board[y][x])

            if not self.isValidNumbers(subBox[i]):
                return False

            if not self.isValidNumbers(cols[i]):
                return False

        return True
