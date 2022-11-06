def __init__(self, k: int, nums: List[int]):
    self.index = k
    self.arr = sorted(nums, reverse=True)

def add(self, val: int) -> int:
    l = len(self.arr)
    i = 0
    while i < l:
        if self.arr[i] <= val:
            self.arr.insert(i, val)
            break
        i += 1
    if len(self.arr) == l:
        self.arr.append(val)
    return self.arr[self.index - 1]
