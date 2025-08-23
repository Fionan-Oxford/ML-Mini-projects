# type : ignore

"""
You are given an n x n grid where we place some 1 x 1 x 1 cubes that are axis-aligned with the x, y, and z axes.
Each value v = grid[i][j] represents a tower of v cubes placed on top of the cell (i, j).
We view the projection of these cubes onto the xy, yz, and zx planes.
A projection is like a shadow, that maps our 3-dimensional figure to a 2-dimensional plane.
We are viewing the "shadow" when looking at the cubes from the top, the front, and the side.
Return the total area of all three projections.
"""
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        area = 0

        area += self._area_top(grid)
        area += self._area_front(grid)
        area += self._area_side(grid)

        return area

    def _area_top(self, grid: List[List[int]]) -> int:
        top_area = 0
        for row in grid:
            for item in row:
                top_area += min(1, item)

        return top_area

    def _area_front(self, grid: List[List[int]]) -> int:
        front_area = 0

        for row in grid:
            front_area += max(row)

        return front_area

    def _area_side(self, grid: List[List[int]]) -> int:

        max_side = grid[0]

        for row in grid:
            for count, value in enumerate(row):
                if value > max_side[count]:
                    max_side[count] = value

        return sum(max_side)


mySolution = Solution()
grid = [[1, 0], [0, 2]]

print(mySolution.projectionArea(grid))

#
