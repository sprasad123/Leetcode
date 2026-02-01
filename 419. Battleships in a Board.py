class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "X":
                    count += 1
                    def dfs(row, col):
                        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                            return
                        if board[row][col] == ".":
                            return
                        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
                        for dx, dy in dirs:
                            if 0 <= row + dx < len(board) and 0 <= col + dy < len(board[0]) and board[row+dx][col+dy] == "X":
                                board[row+dx][col+dy] = "O"
                                dfs(row+dx, col+dy)
                    dfs(row, col)
        return count
        