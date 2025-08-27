"""Given a binary matrix and find the upper-left corner of the largest square of 1's.
follow-up question was: What if we are allowed to switch at most k zeros to 1's?"""

grid = [
    [0, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1],
]


def findLargestSquare(grid: list[list[int]]) -> tuple[int, int]:

    R, C = len(grid), len(grid[0])

    dp: list[list[int]] = [[0] * (C + 1) for _ in range(R + 1)]

    for r in range(R - 1, -1, -1):
        for c in range(C - 1, -1, -1):
            if grid[r][c] == 1:
                dp[r][c] = min(dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1]) + 1

    output = (0, 0)
    largest = 0
    for i in range(R):
        for j in range(C):
            test = dp[i][j]
            if test > largest:
                output = (i, j)
                largest = test

    return output


print(findLargestSquare(grid))
