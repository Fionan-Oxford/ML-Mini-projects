"""Given an array nums of distinct integers
return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        perms: List[List[int]] = []
        n = len(nums)

        def backtrack(path: List[int], remaining: List[int]) -> None:

            if len(path) == n:
                perms.append(path.copy())
                return

            for i, num in enumerate(remaining):
                path.append(num)
                backtrack(path, remaining[:i] + remaining[i + 1 :])
                path.pop()

        backtrack([], nums)
        return perms


nums = [1, 2, 3]
mySolution = Solution()
print(mySolution.permute(nums))
