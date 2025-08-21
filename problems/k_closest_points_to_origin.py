"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""

import heapq
from typing import List
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap: List[tuple[float, List[int]]] = []
        result: List[List[int]] = []
        origin = [0, 0]

        for point in points:
            distance = math.sqrt((point[0] - origin[0]) ** 2 + (point[1] - origin[1]) ** 2)
            heapq.heappush(heap, (distance, point))

        for _ in range(k):
            _, point = heapq.heappop(heap)
            result.append(point)
        return result


mySolution = Solution()
points = [[1, 3], [-2, 2]]
k = 1

points2 = [[3, 3], [5, -1], [-2, 4]]
k2 = 2

print(mySolution.kClosest(points, k))
print(mySolution.kClosest(points2, k2))
