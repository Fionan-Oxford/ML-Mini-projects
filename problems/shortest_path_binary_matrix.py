class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        start = (0, 0)
        R, C = len(grid), len(grid[0])
        dest = (R - 1, C - 1)
        if grid[start[0]][start[1]] == 1 or grid[dest[0]][dest[1]] == 1:
            return -1  # Start or Dest is blocked

        parents: dict[tuple[int, int], tuple[int, int] | None] = {start: None}
        distance: dict[tuple[int, int], int] = {start: 0}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        queue = deque([start])

        while queue:
            curr = queue.popleft()

            if curr == dest:
                break

            cx, cy = curr
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in distance and grid[nx][ny] == 0:
                    parents[(nx, ny)] = curr
                    distance[(nx, ny)] = distance[curr] + 1
                    queue.append((nx, ny))

        # Don't need to rebuild the path
        if dest in distance:
            return distance[dest] + 1  # need to represent jumping out of the grid
        else:
            return -1
