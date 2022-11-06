def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    merged = []
    for m in matrix:
        merged.extend(m)
    heapq.heapify(merged)
    while k - 1:
        heapq.heappop(merged)
        k -= 1
    return heapq.heappop(merged)
