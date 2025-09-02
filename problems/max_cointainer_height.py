"""You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        left, right = 0, n - 1
        left_height, right_height = 0, 0
        max_area = 0

        while left < right:
            left_height = height[left]
            right_height = height[right]
            max_area = max(max_area, (right - left) * min(left_height, right_height))

            if left_height < right_height:
                left += 1
            else:
                right -= 1

        return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
mySolution = Solution()
print(mySolution.maxArea(height))
