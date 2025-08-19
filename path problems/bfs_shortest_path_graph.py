from collections import deque

edges = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 1),
    (4, 0),
    (4, 5),
]

graph: dict[int, list[int]] = {}
for node in range(0, 6):
    graph[node] = []

for u, v in edges:
    graph[u].append(v)  # Directed graph

print(graph)


def bfs_sp(graph: dict[int, list[int]], start: int, dest: int) -> list[int]:

    if start == dest:
        print("start == dest")
        return []

    if start not in graph or dest not in graph:
        print("start or dest not in graph")

        return []

    visited: set[int] = {start}
    parent: dict[int, int | None] = {start: None}
    queue = deque([start])

    while queue:

        current = queue.popleft()

        if current == dest:
            break

        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(neighbour)
                parent[neighbour] = current
                visited.add(neighbour)

    # reconstruct path
    if dest not in parent:
        return []

    path: list[int] = []
    curr: int | None = dest
    while curr is not None:
        path.append(curr)
        curr = parent[curr]

    print(path)
    return path[::-1]


path = bfs_sp(graph, 0, 5)

for step in path:
    print(step)
