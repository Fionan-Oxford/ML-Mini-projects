"""1514. Path with Maximum Probability
You are given an undirected weighted graph of n nodes (0-indexed),
represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b
with a probability of success of traversing that edge succProb[i].

Given two nodes start and end,
find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0.
Your answer will be accepted if it differs from the correct answer by at most 1e-5.


Example 1:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Example 2:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000

Example 3:
Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2."""

from typing import List
import heapq


class Solution:
    def maxProbability(
        self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int
    ) -> float:

        if start_node == end_node:
            return 1.0

        adj: dict[int, list[tuple[float, int]]] = {i: [] for i in range(n)}

        for i, (start, end) in enumerate(edges):
            adj[start].append((succProb[i] * -1, end))
            adj[end].append((succProb[i] * -1, start))

        heap: list[tuple[float, int]] = []
        heapq.heappush(heap, (-1.0, start_node))
        distance: dict[int, float] = {start: -1.0}

        while heap:
            distance_c, node_c = heapq.heappop(heap)

            for cost_n, node_n in adj[node_c]:  # Look at all the neighbours
                distance_n = abs(distance_c * cost_n) * -1  # ensure it is negative

                if distance.get(node_n):
                    if distance[node_n] <= distance_n:
                        continue

                distance[node_n] = distance_n
                heapq.heappush(heap, (distance_n, node_n))

        # Get result
        if end_node not in distance:
            return 0.0
        else:
            return abs(distance[end_node])


mySolution = Solution()
n = 5
edges = [[1, 4], [2, 4], [0, 4], [0, 3], [0, 2], [2, 3]]
succProb = [0.37, 0.17, 0.93, 0.23, 0.39, 0.04]
start = 3
end = 4
print(mySolution.maxProbability(n, edges, succProb, start, end))
