class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        m = len(board[0])
        def isValidRow():
            for row in range(n):
                seen = set()
                for col in range(m):
                    if board[row][col] in seen:
                        return False
                    if "." not in board[row][col]:
                        seen.add(board[row][col])
            return True
        def isValidColumn():
            for col in range(m):
                seen = set()
                for row in range(n):
                    if board[row][col] in seen:
                        return False
                    if "." not in board[row][col]:
                        seen.add(board[row][col])
            return True
        def isValidSubBox(row, col):
            seen = set()
            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    if board[r][c] in seen:
                        return False
                    if "." not in board[r][c]:
                        seen.add(board[r][c])
            return True
        def visitSubBox():
            for r in range(3):
                for c in range(3):
                    if not isValidSubBox(r * 3, c * 3):
                        return False
            return True
        return isValidRow() and isValidColumn() and visitSubBox()