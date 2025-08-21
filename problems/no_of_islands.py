from typing import List, Tuple
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        R, C = len(grid), len(grid[0])
        directions: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = set()
        islands = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1" and (r, c) not in seen:
                    islands += 1
                    q = deque([(r, c)])
                    seen.add((r, c))

                    # BFS flood-fill to mark the whole island
                    while q:
                        x, y = q.popleft()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == "1" and (nx, ny) not in seen:
                                seen.add((nx, ny))
                                q.append((nx, ny))
        return islands


# Example 1 -> 1
grid1 = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
print(Solution().numIslands(grid1))

# Example 2 -> 3
grid2 = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
print(Solution().numIslands(grid2))
