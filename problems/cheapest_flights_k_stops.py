"""787. Cheapest Flights Within K Stops

There are n cities connected by some number of flights.
You are given an array flights where
flights[i] = [fromi, toi, pricei]
indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k,
return the cheapest price from src to dst with at most k stops.
If there is no such route, return -1.


Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops."""

from typing import List
import heapq
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj: dict[int, list[tuple[int, int]]] = {i: [] for i in range(n)}

        # Build the adjacency list
        for node, dest, cost in flights:
            adj[node].append((dest, cost))

        heap: list[tuple[int, int, int]] = []
        heapq.heappush(heap, (0, 0, src))

        distance: dict[tuple[int, int], int] = {(src, 0): 0}

        parent: dict[int, int | None] = {src: None}

        while heap:
            distance_c, stops_c, current = heapq.heappop(heap)

            if distance_c > distance.get((current, stops_c), float("inf")):
                continue

            for neighbour, cost in adj[current]:

                distance_n = distance_c + cost
                stops_n = stops_c + 1

                if stops_n > k + 1:
                    continue

                if distance_n < distance.get((neighbour, stops_n), float("inf")):
                    distance[(neighbour, stops_n)] = distance_n
                    parent[neighbour] = current
                    heapq.heappush(heap, (distance_n, stops_n, neighbour))

        candidates = [c for (node, s), c in distance.items() if node == dst and s <= k + 1]
        return min(candidates) if candidates else -1


mySolution = Solution()
n = 2
flights = [[1, 0, 5]]
src = 0
dst = 1
k = 1

print(mySolution.findCheapestPrice(n, flights, src, dst, k))
