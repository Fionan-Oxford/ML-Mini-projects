from typing import List
from collections import deque

# Find the number of closed islands
# Start with bfs flood fill. However

# We will make a global seen set. I will iterate from top left, making islands using bfs flood fill.
# Every time I see an island, I shall increase the island count. However if I add a danger square (an edge)
# during the flood fill. I lose the count. Either way I complete the floow fill.


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        start = (0, 0)
        self.grid = grid
        num_islands = 0
        self.visited: set[tuple[int, int]] = set([start])

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0 and (x, y) not in self.visited:
                    new = self.flood_fill((x, y))
                    if new:
                        num_islands += 1
        return num_islands

    def check_open(self, pos: tuple[int, int]) -> bool:
        """Check if this position opens the island"""
        x, y = pos
        if x == 0 or x == len(self.grid) - 1 or y == 0 or y == len(self.grid[0]) - 1:
            return True

        return False

    def flood_fill(self, start: tuple[int, int]) -> bool:
        """Update the global seen set"""
        if not self.check_open(start):
            closed = True

        queue = deque([start])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        while queue:
            current = queue.popleft()
            if self.check_open(current):
                closed = False  # Takes one edge to contamintate entire island

            cx, cy = current
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if (
                    0 <= nx < len(self.grid)
                    and 0 <= ny < len(self.grid[0])
                    and (nx, ny) not in self.visited
                    and self.grid[nx][ny] == 0
                ):
                    queue.append((nx, ny))
                    self.visited.add((nx, ny))

        return closed


mySolution = Solution()
grid = [
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0],
]

print(mySolution.closedIsland(grid))
