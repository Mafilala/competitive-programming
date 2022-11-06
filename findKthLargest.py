def findKthLargest(self, nums: List[int], k: int) -> int:
    cp = [-n for n in nums]
    heapq.heapify(cp)
    while k - 1:
        heapq.heappop(cp)
        k -= 1
    return -cp[0]
