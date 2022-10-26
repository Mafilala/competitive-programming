 def __init__(self):
        self.li = []

    def push(self, x: int) -> None:
        self.li.append(x)

    def pop(self) -> int:
        return self.li.pop(0)

    def peek(self) -> int:
        return self.li[0]

    def empty(self) -> bool:
        return False if self.li else True
