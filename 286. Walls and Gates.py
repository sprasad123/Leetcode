from collections import deque
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms or not rooms[0]:
            return

        EMPTY = 2147483647
        GATE = 0
        rows, cols = len(rooms), len(rooms[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == GATE:
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()

            for dx, dy in directions:
                r, c = row + dx, col + dy

                if r < 0 or c < 0 or r >= rows or c >= cols:
                    continue

                if rooms[r][c] != EMPTY:
                    continue

                rooms[r][c] = rooms[row][col] + 1
                queue.append((r, c))
                