from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        perimeter += self._top_bottom_sweep(grid)
        perimeter += self._left_right_sweep(grid)

        return perimeter

    def _top_bottom_sweep(self, grid: List[List[int]]) -> int:

        tb_per = 0

        sweep = [0 for _ in range(len(grid[0]))]

        for row in grid:
            for count, value in enumerate(row):
                tb_per += abs(sweep[count] - value)
            sweep = row

        tb_per += sum(sweep)
        return tb_per

    def _left_right_sweep(self, grid: List[List[int]]) -> int:
        lr_per = 0

        sweep = [0 for _ in range(len(grid))]
        grid_t = map(list, zip(*grid))

        for row in grid_t:
            for count, value in enumerate(row):
                lr_per += abs(sweep[count] - value)
            sweep = row

        lr_per += sum(sweep)
        return lr_per


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
grid = [[1, 0]]


mySolution = Solution()
print(mySolution.islandPerimeter(grid))
