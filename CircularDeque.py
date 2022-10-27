class MyCircularDeque:

    def __init__(self, k: int):
        self.li = [None] * k
        self.front = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.li[self.front] = value
            self.front += 1
            return True
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.li.insert(0, value)
        self.li.pop()
        self.front += 1
        return True
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.li[self.front - 1] = None
        self.front -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.li.pop(0)
        self.li.append(None)
        self.front -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        print(self.front)
        return self.li[self.front - 1]
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.li[0]

    def isEmpty(self) -> bool:
        return self.li.count(None) == self.capacity

    def isFull(self) -> bool:
        return self.li.count(None) == 0
        
