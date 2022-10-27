    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-c for c in counts.values()]
        heapq.heapify(max_heap)
        
        d = deque()
        time = 0
        
        while max_heap or d:
            time += 1
            if max_heap:
                temp = heapq.heappop(max_heap) + 1
                if temp:
                    d.append([temp, time + n])
            if d and d[0][1] == time:
                a_temp = d.popleft()[0]
                heapq.heappush(max_heap, a_temp)
        return time
