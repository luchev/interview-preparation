# Complexity (n = nodes in linked list)
# Time complexity for init: O(1)
# Time complexity for getRandom: O(n) using Reservoir sampling
# Space complexity: O(1)

from typing import List
import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.

        Using Reservoir sampling
        """
        count = 1
        chosen = -1
        node = self.head

        while node:
            if random.random() < 1/count:
                chosen = node.val
            node = node.next
            count += 1
        return chosen
