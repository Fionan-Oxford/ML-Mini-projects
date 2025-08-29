"""Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        perms: List[List[int]] = []
        n = len(nums)

        def backtrack(path: List[int], remaining: List[int]) -> None:

            if len(path) == n:
                perms.append(path.copy())

            for i, num in enumerate(remaining):

                if i > 0:
                    if num == remaining[i - 1]:
                        continue  # duplicate number

                path.append(num)
                backtrack(path, remaining[i + 1 :] + remaining[:i])
                path.pop()

        backtrack([], nums)
        return perms


nums = [1, 2, 3]
mySolution = Solution()
print(mySolution.permuteUnique(nums))
