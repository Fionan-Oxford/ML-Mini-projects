# type: ignore
"""
There are n cities. Some of them are connected, while some are not.
If city a is connected directly with city b,
and city b is connected directly with city c,
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected
cities and no other cities outside of the group.

You are given an n x n matrix isConnected
where isConnected[i][j] = 1 if the ith city and the jth city are directly connected,
and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:

Input: isConnected = [[1,1,0],
                      [1,1,0],
                      [0,0,1]]
Output: 2
Example 2:

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]"""

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n, m = len(isConnected), len(isConnected[0])
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.count = n

        for i in range(n):
            for j in range(m):
                if isConnected[i][j] == 1:
                    self.union(i, j)

        return self.count

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path Compression

        return self.parent[x]

    def union(self, a, b):

        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False  # Already connected

        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.count -= 1
        return True


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
mySolution = Solution()
print(mySolution.findCircleNum(isConnected))
