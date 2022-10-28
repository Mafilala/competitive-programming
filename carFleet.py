def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    fleet_count = len(position)
    twin = [[-p, s] for p, s in zip(position, speed)]
    heapq.heapify(twin)
    front_pos, front_speed = heapq.heappop(twin)
    front_dist = target + front_pos
    front_time = front_dist / front_speed
    while twin:
        pos, spe = heapq.heappop(twin)
        dist = target + pos
        time = dist / spe
        if front_time >= time:
            fleet_count -= 1
        else:
            front_time = time
    return fleet_count
