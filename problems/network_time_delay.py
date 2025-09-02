"""You are given a network of n nodes, labeled from 1 to n.
You are also given times,
a list of travel times as directed edges times[i] = (ui, vi, wi),
where ui is the source node, vi is the target node,
and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.



Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1


Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)"""

import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        #           source     weight dest
        graph: dict[int, list[tuple[int, int]]] = {u: [] for u in range(1, n + 1)}

        for u, v, w in times:
            graph[u].append((v, w))

        distance: dict[int, int] = {u: -1 for u in range(1, n + 1)}
        distance[k] = 0

        def djikstra_fill(start: int) -> None:

            heap: list[tuple[int, int]] = []
            heapq.heappush(heap, (0, start))

            while heap:
                c_distance, current = heapq.heappop(heap)

                for neighbour, n_weight in graph[current]:

                    this_disance = c_distance + n_weight
                    if distance[neighbour] == -1 or distance[neighbour] > this_disance:
                        distance[neighbour] = this_disance

                        heapq.heappush(heap, (distance[neighbour], neighbour))

        djikstra_fill(k)

        max_time = 0
        for _, dist in distance.items():
            if dist == -1:
                max_time = -1
                break
            max_time = max(max_time, dist)

        # Return minimum time for all nodes to receive
        # We need to djikstra for every node,
        # and return the node with the   largest cost
        return max_time


mySolution = Solution()
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(mySolution.networkDelayTime(times, n, k))
