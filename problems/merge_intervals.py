"""Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104"""

from typing import List


# intervals = [[1,3],[2,6],[6,10],[15,18]]
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        out: List[List[int]] = []
        n = len(intervals)
        current_edge = -1

        for i, interval in enumerate(intervals):
            starti, endi = interval
            if starti <= current_edge:
                continue

            for startj, endj in intervals[i + 1 :]:
                if startj <= endi:
                    endi = endj
            out.append([starti, endi])
            current_edge = endi
        return out


intervals = [[1, 3], [2, 6], [6, 10], [15, 18]]
mySolution = Solution()

print(mySolution.merge(intervals))
