"""There are a total of numCourses courses you have to take,
labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1.
So it is impossible."""

from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)

        for course, preq in prerequisites:
            adj[course].append(preq)

        done: set[int] = set()
        visiting: set[int] = set()

        def dfs(c: int) -> bool:

            if c in done:
                return True  # Already done

            if c in visiting:
                return False  # Cycle detected

            visiting.add(c)

            for p in adj[c]:
                if not dfs(p):
                    return False

            visiting.remove(c)
            done.add(c)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


numCourses = 2
prerequisites = [[1, 0]]

mySolution = Solution()
print(mySolution.canFinish(numCourses, prerequisites))
