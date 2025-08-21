"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
"""

from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        start = (0, 0)
        R, C = len(grid), len(grid[0])
        dest = (R - 1, C - 1)
        if grid[start[0]][start[1]] == 1 or grid[dest[0]][dest[1]] == 1:
            return -1  # Start or Dest is blocked

        parents: dict[tuple[int, int], tuple[int, int] | None] = {start: None}
        distance: dict[tuple[int, int], int] = {start: 0}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        queue = deque([start])

        while queue:
            curr = queue.popleft()

            if curr == dest:
                break

            cx, cy = curr
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in distance and grid[nx][ny] == 0:
                    parents[(nx, ny)] = curr
                    distance[(nx, ny)] = distance[curr] + 1
                    queue.append((nx, ny))

        # Don't need to rebuild the path
        if dest in distance:
            return distance[dest] + 1  # need to represent jumping out of the grid
        else:
            return -1


grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]

mySolution = Solution()
print(mySolution.shortestPathBinaryMatrix(grid))
