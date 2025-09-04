"""Example 1:

Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5."""

from typing import List
import math


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m = len(nums1)
        n = len(nums2)

        mn = m + n
        even_length = True

        if mn % 2 > 0:
            even_length = False

        left, right = 0, 0

        half = math.ceil(mn / 2)
        if even_length:
            half += 1

        merged_array = [0.0 for _ in range(half)]

        # lets make a merged array that's just long enough
        for i in range(half):
            if left == m:
                merged_array[i] = nums2[right]
                right += 1
                continue

            if right == n:
                merged_array[i] = nums1[left]
                left += 1
                continue

            if nums1[left] <= nums2[right]:
                merged_array[i] = nums1[left]
                left += 1
                continue

            if nums1[left] > nums2[right]:
                merged_array[i] = nums2[right]
                right += 1
                continue

            raise RuntimeError("Something has gone wrong")

        # we now have a sorted array
        return (merged_array[-1] + merged_array[-2]) / 2 if even_length else merged_array[-1]


mySolution = Solution()
nums1 = []
nums2 = [1]

print(mySolution.findMedianSortedArrays(nums1, nums2))
