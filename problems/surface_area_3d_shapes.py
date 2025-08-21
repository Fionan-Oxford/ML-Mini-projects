"""
You are given an n x n grid where you have placed some 1 x 1 x 1 cubes.
Each value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).
After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.
Return the total surface area of the resulting shapes.
Note: The bottom face of each shape counts toward its surface area.
"""

from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:

        surface_area = 0
        surface_area += self._surfaceBottomTop(grid)
        surface_area += self._surfaceFrontBack(grid)
        surface_area += self._surfaceLeftRight(grid)

        return surface_area

    def _surfaceBottomTop(self, grid: List[List[int]]) -> int:

        print(sum([min(1, v) for row in grid for v in row]) * 2)
        return sum([min(1, v) for row in grid for v in row]) * 2  # Top will always be same as bottom

    def _surfaceFrontBack(self, grid: List[List[int]]) -> int:

        front_back_area = 0
        sweep = [0 for _ in range(len(grid))]  # Start with all zeroes

        for row in grid:
            differences = [abs(row[i] - sweep[i]) for i in range(len(row))]
            front_back_area += sum(differences)
            sweep = row

        # FInally add the last face
        front_back_area += sum(sweep)

        print(front_back_area)
        return front_back_area

    def _surfaceLeftRight(self, grid: List[List[int]]) -> int:

        left_right_area = 0
        grid_t = map(list, zip(*grid))
        sweep = [0 for _ in range(len(grid[0]))]  # Start with all zeroes

        for row in grid_t:
            differences = [abs(row[i] - sweep[i]) for i in range(len(row))]
            left_right_area += sum(differences)
            sweep = row

        # Finally add the last face
        left_right_area += sum(sweep)

        print(left_right_area)
        return left_right_area


grid = [[1, 2], [3, 4]]

mySolution = Solution()
print(mySolution.surfaceArea(grid))
