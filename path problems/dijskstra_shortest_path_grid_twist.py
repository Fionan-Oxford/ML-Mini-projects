"""
Data Structure: Min-Heap
State: dist map (best cost so far), skip stale heap pops
Expansion Order: By increasing total cost
Early Exit, as soon as you pop the goal from the heap"""

import heapq


def dijkstra_shortest_path_t_b(
    grid: list[list[int]], start: tuple[int, int], dest: tuple[int, int]
) -> list[tuple[int, int]]:
    """
    Find a path from start to dest minimizing energy:
      - Moving to equal or lower cell costs 0
      - Moving to a higher cell costs (dst - src)
    """
    rows, cols = len(grid), len(grid[0])

    # Directions, right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Kick off priority queue
    heap: list[tuple[int, tuple[int, int]]] = []
    parent: dict[tuple[int, int], tuple[int, int] | None] = {}
    distance: dict[tuple[int, int], int] = {}

    for c in range(cols):
        start = (0, c)
        distance[start] = 0
        parent[start] = None
        heapq.heappush(heap, (0, start))

    while heap:
        current_dist, current = heapq.heappop(heap)

        # Skip stale entries
        if current_dist > distance[current]:
            continue

        # Reached any bottom cells -> Optimal
        if current[0] == rows - 1:
            # Reconstruct from this cell
            path: list[tuple[int, int]] = []
            curr: tuple[int, int] | None = dest
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            return path[::-1]

        # Explore directions
        for direction in directions:
            neighbour = (current[0] + direction[0], current[1] + direction[1])

            # IS this in bounds?
            if 0 <= neighbour[0] < rows and 0 <= neighbour[1] < cols:

                # Energy cost rule
                cost = max(0, grid[neighbour[0]][neighbour[1]] - grid[current[0]][current[1]])
                new_dist = current_dist + cost

                # Relaxation step
                if neighbour not in distance or new_dist < distance[neighbour]:
                    distance[neighbour] = new_dist
                    parent[neighbour] = current
                    heapq.heappush(heap, (new_dist, neighbour))

    return []


# Example grid (heights)
grid = [
    [3, 3, 0, 2, 1],
    [2, 4, 3, 2, 3],
    [1, 1, 1, 0, 0],
    [0, 4, 3, 2, 0],
    [0, 0, 3, 1, 2],
]

start = (0, 0)
dest = (4, 4)

path = dijkstra_shortest_path_t_b(grid, start, dest)

if path:
    # Compute total energy along the path
    energy = sum(max(0, grid[r2][c2] - grid[r1][c1]) for (r1, c1), (r2, c2) in zip(path, path[1:]))
    print(f"Shortest path {path} with energy {energy}")
else:
    print("No valid path was found")
