class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclide(arr):
            x = arr[0]
            y = arr[1]
            ans = (x ** 2) + (y ** 2)
            return ans
        ans = []
        for pt in points:
            ans.append([euclide(pt), pt])
        heapq.heapify(ans)
        final_ans = []
        while k > 0:
            po = heapq.heappop(ans)
            final_ans.append(po[1])
            k -= 1
        return final_ans
        
