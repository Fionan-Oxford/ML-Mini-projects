import heapq


def build_graph(n: int, edges: list[tuple[int, int, int]]) -> dict[int, list[tuple[int, int]]]:
    """Directed, weighted adjacency list: graph[u] = [(v, w), ...]."""
    graph: dict[int, list[tuple[int, int]]] = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))
    return graph


def dijkstra_shortest_path(
    graph: dict[int, list[tuple[int, int]]], start: int, dest: int
) -> tuple[list[int], int | None]:
    """
    Dijkstra from `start` to `dest` on a graph with non-negative weights.
    Returns (path, cost). If unreachable, returns ([], None).
    """
    if start not in graph or dest not in graph:
        return [], None
    if start == dest:
        return [start], 0

    dist: dict[int, int] = {start: 0}
    parent: dict[int, int | None] = {start: None}
    heap: list[tuple[int, int]] = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:  # skip stale entry
            continue
        if u == dest:  # early exit is valid (non-negative weights)
            break
        for v, w in graph[u]:
            nd = d + w
            if v not in dist or nd < dist[v]:  # no ∞; absence means unreached
                dist[v] = nd
                parent[v] = u
                heapq.heappush(heap, (nd, v))

    if dest not in dist:
        return [], None

    # Reconstruct path
    path: list[int] = []
    cur: int | None = dest
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    return path[::-1], dist[dest]


# --- Example ---
if __name__ == "__main__":
    edges = [
        (0, 1, 1),
        (0, 2, 2),
        (1, 2, 0),
        (1, 3, 4),
        (2, 3, 2),
        (3, 4, 1),
        (4, 1, 0),
        (4, 0, 4),
        (4, 5, 3),
    ]
    graph = build_graph(6, edges)
    path, cost = dijkstra_shortest_path(graph, 0, 5)
    print("path:", path)  # e.g. [0, 2, 3, 4, 5]
    print("cost:", cost)  # e.g. 8
