# Complexity (n = number of items in nums, k = sliding window size)
# Time complexity: O(n)
# Space complexity: O(k)

from typing import List
import math

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = Queue()
        for x in nums[:k]:
            que.push(x)

        maxs = []
        for x in nums[k:]:
            maxs.append(que.pop())
            que.push(x)
        maxs.append(que.pop())

        return maxs

class Stack:
    def __init__(self):
        self.vals = []
        self.maxs = []

    def push(self, x):
        self.vals.append(x)
        if len(self.maxs) == 0:
            self.maxs.append(x)
        else:
            self.maxs.append(max(x, self.maxs[-1]))

    def pop(self):
        return (self.vals.pop(), self.maxs.pop())

    def max(self):
        if self.maxs:
            return self.maxs[-1]
        else:
            return -math.inf


class Queue:
    def __init__(self):
        self.pusher = Stack()
        self.popper = Stack()

    def push(self, x):
        self.pusher.push(x)

    def pop(self):
        if len(self.popper.vals) == 0:
            while len(self.pusher.vals) > 0:
                self.popper.push(self.pusher.pop()[0])
        return max(self.pusher.max(), self.popper.pop()[1])
