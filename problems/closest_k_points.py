class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap: List[tuple[float, List[int]]] = []
        result: List[List[int]] = []
        origin = [0, 0]

        for point in points:
            distance = math.sqrt((point[0] - origin[0]) ** 2 + (point[1] - origin[1]) ** 2)
            heapq.heappush(heap, (distance, point))

        for _ in range(k):
            _, point = heapq.heappop(heap)
            result.append(point)
        return result
