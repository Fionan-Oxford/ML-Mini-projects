"""Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subset: List[List[int]] = []
        n = len(nums)

        def backtrack(start: int, path: List[int]) -> None:
            if start > n:
                return

            subset.append(path.copy())

            for i in range(start, n):
                num = nums[i]
                path.append(num)
                backtrack(i + 1, path)
                path.pop()
            return

        backtrack(0, [])

        return subset


nums = [1, 2, 3]
mySolution = Solution()
print(mySolution.subsets(nums))
