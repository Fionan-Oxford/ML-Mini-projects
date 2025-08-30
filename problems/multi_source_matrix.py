"""Given an m x n binary matrix mat,
return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

Example 1:

Input: mat = [[0,0,0],
              [0,1,0],
              [0,0,0]]

Output:      [[0,0,0],
              [0,1,0],
              [0,0,0]]
Example 2:

Input: mat = [[0,0,0],
              [0,1,0],
              [1,1,1]]

Output:      [[0,0,0],
              [0,1,0],
              [1,2,1]]"""

from typing import List
from collections import deque


from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        R, C = len(mat), len(mat[0])
        q = deque()
        dist = [[float("inf")] * C for _ in range(R)]

        for r in range(R):
            for c in range(C):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    q.append((r, c))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        return dist


mat = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1],
]
mySolution = Solution()
print(mySolution.updateMatrix(mat))
