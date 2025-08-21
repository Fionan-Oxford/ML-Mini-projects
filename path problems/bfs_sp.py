import heapq


def djik_g_sp(grid: list[list[int]]) -> list[tuple[int, int]]:
    """Doc string"""
    rows, cols = len(grid), len(grid[0])

    heap: list[tuple[int, tuple[int, int]]] = []
    distance: dict[tuple[int, int], int] = {}
    parent: dict[tuple[int, int], tuple[int, int] | None] = {}

    for c in range(cols):
        start = (0, c)
        distance[start] = 0
        parent[start] = None
        heapq.heappush(heap, (0, start))

    while heap:
        curr_distance, current = heapq.heappop(heap)

        if curr_distance > distance[current]:
            continue

        # End Condition
        if current[0] == rows - 1:
            path: list[tuple[int, int]] = []
            curr: tuple[int, int] | None = current

            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            return path[::-1]

        # Explore
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dir in directions:
            neighbour = (current[0] + dir[0], current[1] + dir[1])

            # In bounds?
            if 0 <= neighbour[0] < rows and 0 <= neighbour[1] < cols:

                # Calculate energy
                energy = max(0, grid[neighbour[0]][neighbour[1]] - grid[current[0]][current[1]])
                new_dist = curr_distance + energy

                # Relaxation step
                if neighbour not in distance or new_dist < distance[neighbour]:
                    distance[neighbour] = new_dist
                    parent[neighbour] = current
                    heapq.heappush(heap, (new_dist, neighbour))
    return []


grid = [
    [3, 3, 0, 2, 1],
    [2, 4, 3, 2, 3],
    [1, 1, 1, 0, 0],
    [0, 4, 3, 2, 0],
    [0, 0, 3, 1, 2],
]

path = djik_g_sp(grid)
print(path)
