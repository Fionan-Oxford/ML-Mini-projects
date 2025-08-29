"""Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        comb: List[List[int]] = []
        n = len(candidates)

        def dfs(start: int, path: List[int], sub_target: int) -> None:

            if sub_target == 0:
                comb.append(path.copy())
                return

            for i in range(start, n):

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                c = candidates[i]

                if c > sub_target:
                    break  # Sorted so all the rest will be greater

                path.append(c)
                dfs(i + 1, path, sub_target - c)
                path.pop()

        dfs(0, [], target)

        return comb


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8

mySolution = Solution()
print(mySolution.combinationSum2(candidates, target))
