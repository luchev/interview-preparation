# Complexity (n = capacity)
# Time complexity: O(n)
# Space complexity: O(1) per operation

from typing import List

class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [0] * k
        self.front = -1
        self.end = 0
        self.size = 0
        self.cap = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.front = (self.front + 1) % self.cap
        self.data[self.front] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.end = (self.end + 1) % self.cap
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.end]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
