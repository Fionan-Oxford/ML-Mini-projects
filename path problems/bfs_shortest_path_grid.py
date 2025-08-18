"""
Data Structure: FIFO Queue
State: Visited set (first time you see a node is the best)
Expansion Order: Layer by Layer
Early Exit, as soon as you deque the goal"""

from collections import deque


def bfs_shortest_path(grid: list[list[int]], start: tuple[int, int], dest: tuple[int, int]) -> list[tuple[int, int]]:

    if grid[start[0]][start[1]] == 1 or grid[dest[0]][dest[1]] == 1:
        return []

    # Directions, right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Kick off bfs
    queue = deque([start])
    parent: dict[tuple[int, int], tuple[int, int] | None] = {start: None}
    visited: set[tuple[int, int]] = {start}

    while queue:
        current = queue.popleft()
        if current == dest:
            break

        # Explore directions
        for dx, dy in directions:
            neighbour = (current[0] + dx, current[1] + dy)

            # IS this bound or blocked
            if (
                0 <= neighbour[0] < len(grid)
                and 0 <= neighbour[1] < len(grid[0])
                and neighbour not in visited
                and grid[neighbour[0]][neighbour[1]] == 0
            ):
                parent[neighbour] = current
                visited.add(neighbour)
                queue.append(neighbour)

    if dest not in parent:
        return []

    path: list[tuple[int, int]] = []
    curr: tuple[int, int] | None = dest
    while curr is not None:
        path.append(curr)
        curr = parent[curr]

    return path[::-1] if path[-1] == start else []


# Example grid (0 = passable, 1 = blocked)

grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

start = (0, 0)
dest = (3, 3)

path = bfs_shortest_path(grid, start, dest)

if path:
    print(f"Shortest path {path}")
else:
    print(f"No valid path was found")
