from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])

        dp: list[list[int]] = [[0] * (C + 1) for _ in range(R + 1)]

        square_side = 0
        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                if matrix[r][c] == "1":
                    dp[r][c] = min(dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1]) + 1
                    square_side = max(square_side, dp[r][c])

        return square_side * square_side


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]

mySolution = Solution()
print(mySolution.maximalSquare(matrix))
