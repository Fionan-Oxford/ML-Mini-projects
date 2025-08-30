"""Given n non-negative integers representing
an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.



Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9"""

from typing import List


class Solution2:
    def trap2(self, height: List[int]) -> int:

        trapped_water = 0

        def water_point_n(this_pos: int) -> int:

            this_height = height[this_pos]
            max_left, max_right = 0, 0

            for i in range(this_pos - 1, -1, -1):
                max_left = max(max_left, height[i])

            for k in range(this_pos + 1, len(height)):
                max_right = max(max_right, height[k])

            water = max(0, min(max_left - this_height, max_right - this_height))
            return water

        for n in range(len(height)):
            trapped_water += water_point_n(n)

        return trapped_water


# Below is a faster two_pointers solution


class Solution:
    def trap(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0

        trapped_water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    trapped_water += left_max - height[left]

                left += 1

            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    trapped_water += right_max - height[right]

                right -= 1

        return trapped_water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
mySolution = Solution()
print(mySolution.trap(height))
# expect 11
