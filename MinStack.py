class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        if self.arr:
            self.arr.pop()

    def top(self) -> int:
        if self.arr:
            return self.arr[-1]

    def getMin(self) -> int:
        return min(self.arr)
