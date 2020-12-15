# Complexity (n = number nodes in the linked list)
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def plusOneCarry(head: ListNode):
            if head is None:
                return ListNode(1)

            if head.next is None:
                head.val += 1
            else:
                head.val += plusOneCarry(head.next)

            if head.val == 10:
                head.val = 0
                return 1
            return 0

        carry = plusOneCarry(head)
        if carry == 1:
            return ListNode(1, head)
        return head
